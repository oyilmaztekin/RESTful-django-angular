/***
 *     .d88888b. 8888888888P 8888888888 8888888b.  
 *    d88P" "Y88b      d88P  888        888   Y88b 
 *    888     888     d88P   888        888    888 
 *    888     888    d88P    8888888    888   d88P 
 *    888     888   d88P     888        8888888P"  
 *    888     888  d88P      888        888 T88b   
 *    Y88b. .d88P d88P       888        888  T88b  
 *     "Y88888P" d8888888888 8888888888 888   T88b 
 *                                                 
 *                                                 
 *                                                 
 */
// Özer Yılmaztekin
// yilmaztekin.ozer@gmail.com


(function(window,document){
	'use strict';
	console.log(`%c
888                                                             d8b 
888                                                             Y8P 
888                                                                 
88888b.  .d88b. 888  888 8888b. 88888888 .d88b.  .d88b. 88888888888 
888 "88bd8P  Y8b888  888    "88b   d88P d88P"88bd8P  Y8b   d88P 888 
888  88888888888888  888.d888888  d88P  888  88888888888  d88P  888 
888 d88PY8b.    Y88b 888888  888 d88P   Y88b 888Y8b.     d88P   888 
88888P"  "Y8888  "Y88888"Y88888888888888 "Y88888 "Y8888 88888888888 
                     888                     888                    
                Y8b d88P                Y8b d88P                    
                 "Y88P"                  "Y88P"       "                                                       
`, "font-family:monospace; font-size:8px; color:#efefef; background-color:blue; padding:3px;")
	//console.log("%c Halkla İlişkiler Front-End ;)", 'color: #efefef; background-color: blue; font-size: 10px; padding: 3px;');
	console.log("%c Workflows: Gulp, SASS, Bootstrap, Angularjs", 'color: #323232; background-color: #efefef; font-size: 12px; padding: 3px;');
	
	$(window).on('load', function() {
		if (window.location.hash === "#!/"){
  			$("#container-landing .landing___").removeAttr('id');
			$("#container-landing .landing___").attr('id', 'landing');
			$("#ui-view-landing").show();
			$("#ui-view").hide();
		}

		else if (window.location.hash !== "#!/") {
			$("#container-landing .landing___").removeAttr('id');
			$("#container-landing .landing___").attr('id', 'ic-landing');
			$("#ui-view-landing").hide();
			$("#ui-view").show();
			
		}
	});

	window.addEventListener("hashchange",function(event){
  		if (window.location.hash === "#!/"){
  			$("#container-landing .landing___").removeAttr('id');
			$("#container-landing .landing___").attr('id', 'landing');
			$("#ui-view").toggle();
			$("#ui-view-landing").toggle();
		}

		else if (window.location.hash !== "#!/") {
			$("#container-landing .landing___").removeAttr('id');
			$("#container-landing .landing___").attr('id', 'ic-landing');
			$("#ui-view").toggle();
			$("#ui-view-landing").toggle();
			
			
			
		}
	});

	
})(window,document);