const linebot = require('linebot');
const express = require('express');
const rp = require('request-promise');
const bodyParser = require('body-parser');
 
const SITE_NAME = '���';
const aqiOpt = {
    uri: "http://opendata2.epa.gov.tw/AQI.json",
    json: true
}; 
 
const bot = linebot({
	channelId: process.env.CHANNEL_ID,
	channelSecret: process.env.0ed4045d630e8bd06f997333ffcc7e72,
	channelAccessToken: process.env.mhDgsL1co2B6zyMqPROBjA854E+lyLpx/1BVkyrGN+U/eXlZxn/lY2ytGNxuDWXeW8Xn2p8PTXOSLV4L9JRKWkYQFcuU55/BoNp3qpK+QDbFYaVrN8qq2ZQmcYLuNc9doULqj5g3c3hmYyCtX0xGQwdB04t89/1O/w1cDnyilFU=});
 
function readAQI(repos){
    let data;
    
    for (i in repos) {
        if (repos[i].SiteName == SITE_NAME) {
            data = repos[i];
            break;
        }
    }
 
    return data;
}
 
const app = express();
app.set('view engine', 'ejs');
 
const linebotParser = bot.parser();
 
app.get('/',function(req,res){
    rp(aqiOpt)
    .then(function (repos) {
        res.render('index', {AQI:readAQI(repos)});
    })
    .catch(function (err) {
		res.send("�L�k���o�Ů�~���ơ�");
    });
});
 
app.post('/linewebhook', linebotParser);
 
bot.on('message', function (event) {
	switch (event.message.type) {
		case 'text':
			switch (event.message.text) {
				case '�Ů�':
					let data;
					rp(aqiOpt)
					.then(function (repos) {
						data = readAQI(repos);
						event.reply(data.County + data.SiteName +
						'\n\nPM2.5���ơG'+ data["PM2.5_AVG"] + 
					    '\n���A�G' + data.Status);
					})
					.catch(function (err) {
						event.reply('�L�k���o�Ů�~���ơ�');
					});
					break;
 
				case 'Me':
					event.source.profile().then(function (profile) {
						return event.reply('Hello ' + profile.displayName + ' ' + profile.userId);
					});
					break;
			}
			break;
		case 'sticker':
			event.reply({
				type: 'sticker',
				packageId: 1,
				stickerId: 1
			});
			break;
		default:
			event.reply('Unknow message: ' + JSON.stringify(event));
			break;
	}
});
 
app.listen(process.env.PORT || 80, function () {
	console.log('LineBot is running.');
});