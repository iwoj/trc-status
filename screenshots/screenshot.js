var dateObj = new Date();
var month = dateObj.getUTCMonth() + 1; //months from 1-12
var day = dateObj.getUTCDate();
var year = dateObj.getUTCFullYear();

newdate = year + "-" + month + "-" + day;

var delay = 10;

var page = require('webpage').create();
page.viewportSize = {
    width: 1920,
    height: 1080
};
page.clipRect = { top: 0, left: 0, width: 1920, height: 1080 };
page.zoomFactor = 1.5;
page.open('https://trcprogressbar.ca/', function() {
    window.setTimeout(function() {
          page.render('trcprogressbar-'+newdate+'.png');
          phantom.exit();
        }, delay * 1000);
});

