$(document).ready(function() {
	//if job changes, execute
	$("input[name='job']").change(function(){
		calcHP();
	});
	$(document).on('click','input[type=number]',function(){ this.select(); });

	//preselect a class and a fight to avoid issues (order matters to display correct values

	//$("#fight").val("WoL EX");
	$("#job15").click()
});

// A big thank you to Llillymoo and xephero on reddit for providing these values
//							 Basic   BisEx   Gordias ThordEx Midas   SephEx  A1S     A2S     A3S     A4S     A5S     A6S     A7S     A8S     NidEx   SophEx  A9S     A10S    A11S    A12S    Creator Zurvan  Shinryu Lakshmi Susano  Omega    O1S     O2S     O3S     O4S     ShinEX  Sigma    O5S      O6S     O7S     O8S     Byakko  Tsukyu  Suzaku  Seiryu   O8S      O9S      O10S     O11S     O12S     Eden N   E1S      E2S      E3S      E4S      Titania  Innozen  Hades Ex
var klasse;
var fight;
var groupfight;
var maxTime = 180; //180 seconds max

function limit(value, min, max) {
	if(value > max)
		value = max;
	if (value < min)
		value = min;
	return value;
}

//set remaining time to 0 if restHP were specified
function clearRemTime() {
	$("#remtime").val(0);
}

//set remaining HP to 0 if clearTime was specified
function clearRemHP() {
	$("#remhp").val(0);
}

function updateSelected() {
	klasse=$('input[name="job"]:checked').val();
	fight = $("#fight option:selected").val();
	groupfight = $("#groupfight option:selected").val();

	console.log("Klasse: " + klasse)
	console.log("Fight: " + fight)
	console.log("GroupFight" + groupfight)
}

function calcHP() {
	updateSelected();
	fetch("./jobs_dps.json")
	  .then(response => response.json())
	  .then(json =>
		$("div.dummytext").html("Die Trainingspuppe hat "+json[klasse][fight].toString()+" LP.<br/>Benötigter DPS: " +(parseInt(json[klasse][fight], 10)/180).toFixed(2).toString())
	  );

}

function calcHPgroup() {
	//replace fightid with a new json which maps fightname (O12S) with max hp of the actual boss
	updateSelected();
	fetch("./jobs_dps.json")
	  .then(response => response.json())
	  .then(json =>
		$("div.dummygtext").html("Die Trainingspuppe hat "+json["GruppenHP"][fight].toString()+" LP.<br/>Benötigter DPS: " + json["GruppenDPS"][fight].toString())
	  );
}

function calcDPS() {
	fetch("./jobs_dps.json")
	  .then(response => response.json())
	  .then(json => calcDPS2(json) );
}

function calcDPS2(json) {
	updateSelected();
	var remHP = $("#remhp").val();
	var remTime = $("#remtime").val();

	var dpsText = "";
	if(typeof klasse != 'undefined') {

		remHP = limit(remHP, 0, 100);
		remTime = limit(remTime, 0, 180);
		var bossHP = json[klasse][fight];

		if(bossHP != 0) {
			var dps = (1 - (remHP * 0.01)) * bossHP / (maxTime - remTime)
			dpsText = "Du hast " + dps.toFixed(2).toString() + " DPS erreicht!";

		} else {
			dpsText = "Keine Werte verfügbar für die kombination " + klasse + " und " + fight;
		}
	} else {
		dpsText = "Bitte Wähle zuerst eine Klasse.";
	}

	$("#dpsValue").html(dpsText);
}

function showSingle(){
	$(".singleDPS").css('display', '');
	$(".groupDPS").css('display', 'none');
	$(".infodiv").css('display', 'none');
}

function showGroup(){
	$(".groupDPS").css('display', '');
	$(".singleDPS").css('display', 'none');
	$(".infodiv").css('display', 'none');
}

function showInfo(){
	$(".infodiv").css('display', '');
	$(".singleDPS").css('display', 'none');
	$(".groupDPS").css('display', 'none');
}
