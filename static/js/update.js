$(document).ready(function () {

    var socket = io.connect('http://localhost:9000');

    socket.on('connect', function () {
        socket.send("USER HAS CONNECTED");
    });

    // When "new-chart-data" message is recieved, update chart with data
    socket.on('new-chart-data', function (data) {
        if (temp_chart_created == true) {
            drawTempChart(data)
            var temp_chart_created = true
        } else {
            console.log("Updating chart!")
            console.log(data)
            tempchart.update(data)
        }
    });

    socket.on('message', function (message) {
        $("messages").append('<li>' + message + '</li>');
        console.log("recieved message!");
        console.log(message)
    });

    $("sendbutton").on("click", function () {
        socket.send($('myMessage').val());
    });

    var data = {
        "series": [{
            "name": 'FC1',
            "data": [{
                    "x": 143134652600,
                    "y": 70
                },
                {
                    "x": 143234652600,
                    "y": 70
                }
            ]
        }, {
            "name": 'FC2',
            "data": [{
                    "x": 143134652600,
                    "y": 40
                },
                {
                    "x": 143234652600,
                    "y": 40
                }
            ]
        }, {
            "name": 'FC3',
            "data": [{
                    "x": 143134652600,
                    "y": 25
                },
                {
                    "x": 143234652600,
                    "y": 25
                }
            ]
        }, {
            "name": 'FC4',
            "data": [{
                    "x": 143134652600,
                    "y": 25
                },
                {
                    "x": 0,
                    "y": 25
                }
            ]
        }]
    };
    drawTempChart(data)


});
//Draw Temperature Chart
var tempchart;

function drawTempChart(data) {
    console.log("Drawing chart!")

    var chartlegend = document.getElementById('data-chart-legend');

    var options = {
        axisX: {
            type: Chartist.FixedScaleAxis,
            divisor: 5,
            labelInterpolationFnc: function (value) {
                return moment.unix(value).format('MMM D, h:mm:ss a');
            }
        },
        //width: 960,
        height: 340,
        lineSmooth: false,
        showPoint: false,
        plugins: [
            Chartist.plugins.legend({
                position: chartlegend
            })
        ]
    };
    tempchart = new Chartist.Line('.data-chart', data, options);

}