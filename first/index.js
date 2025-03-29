const FS = require('node:fs');
const PATH = require('node:path');

// Require the necessary discord.js classes
const { Client, Collection, Events, GatewayIntentBits } = require('discord.js');
const { TOKEN } = require('./config.json');

// Create a new client instance
const CLIENT = new Client({ intents: [GatewayIntentBits.Guilds] });

// When the client is ready, run this code (only once).
// The distinction between `client: Client<boolean>` and `readyClient: Client<true>` is important for TypeScript developers.
// It makes some properties non-nullable.
CLIENT.once(Events.ClientReady, readyClient => {
	console.log(`Ready! Logged in as ${readyClient.user.tag}`);
});

// Log in to Discord with your client's token
CLIENT.login(TOKEN);


const FOLDERS_PATH = PATH.join(__dirname, 'commands');
const COMMAND_FOLDERS = FS.readdirSync(FOLDERS_PATH);

for (const FOLDER of COMMAND_FOLDERS) {
	const COMMANDS_PATH = PATH.join(FOLDERS_PATH, FOLDER);
	const COMMAND_FILES = FS.readdirSync(COMMANDS_PATH).filter(file => file.endsWith('.js'));
	for (const FILE of COMMAND_FILES) {
		const FILE_PATH = PATH.join(COMMANDS_PATH, FILE);
		const COMMAND = require(FILE_PATH);
		// Set a new item in the Collection with the key as the command name and the value as the exported module
		if ('data' in COMMAND && 'execute' in COMMAND) {
			CLIENT.commands.set(COMMAND.data.name, COMMAND);
		} else {
			console.log(`[WARNING] The command at ${FILE_PATH} is missing a required "data" or "execute" property.`);
		}
	}
}

CLIENT.on(Events.InteractionCreate, interaction => {
    if (!interaction.isChatInputCommand()) return;
	console.log(interaction);
});