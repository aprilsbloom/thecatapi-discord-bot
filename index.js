require('dotenv').config();
const Discord = require('discord.js');
const axios = require('axios');
const { MessageEmbed } = require('discord.js');

const client = new Discord.Client({ intents: ["GUILDS", "GUILD_MESSAGES"] })

client.on('ready', () => {
    client.user.setActivity(`*help in ${client.guilds.cache.size} Servers `, { type: "LISTENING" })
    console.log(`Logged in as ${client.user.tag}!`);
    console.log();
    console.log('Logs:');
});

const apikeys = ["api-key-here", "api-key-here"]; // i registered for multiple api keys in order to increase the maximum number of requests i can use

const random = Math.floor(Math.random() * apikeys.length);

client.on('messageCreate', async msg => {
    switch (msg.content) {
        case "*gif":
            const img = await getGif(); //fetches an URL from the API
            const exampleEmbed = new MessageEmbed()
                .setColor('#0099ff')
                .setTitle('Here\'s your cat gif:')
                .setURL('https://github.com/micgar19/thecatapi-discord-bot')
                .setImage(img)
                .setTimestamp()
                .setFooter({ text: 'Made by business man#4444', iconURL: 'https://i.imgur.com/1AyUxRE.png' });
            msg.channel.send({ embeds: [exampleEmbed] });
            console.log('User ' + msg.author.tag + ' ID: ' + msg.author.id + ' ran *gif in Channel: #' + msg.channel.name + ' Server: ' + msg.guild.name)
            break;
        case "*image":
            const img1 = await getImage();
            const exampleEmbed1 = new MessageEmbed()
                .setColor('#0099ff')
                .setTitle('Here\'s your cat image:')
                .setURL('https://github.com/micgar19/thecatapi-discord-bot')
                .setImage(img1)
                .setFooter({ text: 'Made by business man#4444', iconURL: 'https://i.imgur.com/1AyUxRE.png' });
            msg.channel.send({ embeds: [exampleEmbed1] });
            console.log('User ' + msg.author.tag + ' ID: ' + msg.author.id + ' ran *image in Channel: #' + msg.channel.name + ' Server: ' + msg.guild.name)
            break;
        case "*help":
            const img2 = await getImage();
            const exampleEmbed2 = new MessageEmbed()
                .setColor('#0099ff')
                .setTitle('Help')
                .setURL('https://github.com/micgar19/thecatapi-discord-bot')
                .addFields({ name: 'Gif', value: '```*gif```Returns a random cat gif.', inline: true }, { name: 'Image', value: '```*image``` to get a random cat image.', inline: true }, )
                .addField('Help', '```*help```Sends this message.', true)
                .setImage(img2)
                .setFooter({ text: 'Made by business man#4444', iconURL: 'https://i.imgur.com/1AyUxRE.png' });
            msg.channel.send({ embeds: [exampleEmbed2] });
            console.log('User ' + msg.author.tag + ' ID: ' + msg.author.id + ' ran *help in Channel: #' + msg.channel.name + ' Server: ' + msg.guild.name)
            break;
    }
})

//add this function below client.on('message' ...
async function getGif() {
    const res = await axios.get('https://api.thecatapi.com/v1/images/search?mime_types=gif', {
        headers: {
            'x-api-key': apikeys[random] // selects a random api key to use, i have 10 so it means my max requests is 100k per month
        }
    });
    return res.data[0].url;
}

async function getImage() {
    const res = await axios.get('https://api.thecatapi.com/v1/images/search', {
        headers: {
            'x-api-key': apikeys[random]
        }
    });
    return res.data[0].url;
}


//make sure this is the last line
client.login(process.env.CLIENT_TOKEN); //login to the bot using the token