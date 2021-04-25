// Retrieve Elements
const consoleLogList = document.querySelector('.editor__console-logs');
const executeCodeBtn = document.querySelector('.editor__run');
const resetCodeBtn = document.querySelector('.editor__reset');

// Setup Ace
let codeEditor = ace.edit("editorCode");
let defaultCode = '#include <stdio.h> \r#include <stdlib.h>\r\rint main(){\r //Write your code here \r}';

let program_files;
var editors = {};
var text_files = [];

var line_numbers = {};
var files_line_numbers = {};
var file_number_id;

var scount = "";

var marker="";

let output_string;

let editorLib = {
    clearConsoleScreen() {

        // Remove all elements in the log list
        while (consoleLogList.firstChild) {
            consoleLogList.removeChild(consoleLogList.firstChild);
        }
    },
    printToConsole(userCode) {
        const newLogItem = document.createElement('li');
        const newLogText = document.createElement('pre');

        newLogText.className = userCode.class;
        newLogText.textContent = userCode;
        newLogItem.appendChild(newLogText);
        consoleLogList.appendChild(newLogItem);
    },
    init(codeEditor) {
        // Configure Ace

        // Theme
        codeEditor.setTheme("ace/theme/dracula");

        // Set language
        codeEditor.session.setMode("ace/mode/c_cpp");

        // Set Options
        codeEditor.setOptions({
            // fontFamily: 'Inconsolata',
            fontSize: '12pt',
            enableBasicAutocompletion: true,
            enableLiveAutocompletion: true,
        });

        // Set Default Code
        codeEditor.setValue(defaultCode);
        codeEditor.gotoLine(5);
    }
}

// Events
// executeCodeBtn.addEventListener('click', () => {
//     // Clear console messages
//     editorLib.clearConsoleScreen();
//     // console.log(program_files)
//     // console.log(editors)

//     // for(var i=0; i< program_files.length; ++i){
//     //     // try{
//     //         console.log(editors[program_files[i]].getValue())
//     //     // }
//     //     // catch{
            
//     //     // }
//     // }
//     // Get input from the code editor
//     // const userCode = codeEditor.getValue();
//     $.getJSON({
//         url: "/json_data_func",
//         success: function(data){
//             editorLib.printToConsole(data.a);
//             // console.log(data.a);
//         }
//     });
    
//     // Run the user code
//     // try {
//     //     // Print to the console
//     //     editorLib.printToConsole(userCode);
//     // } catch (err) {
//     //     console.error(err);
//     // }
// });

// resetCodeBtn.addEventListener('click', () => {
//     // Clear ace editor
//     codeEditor.setValue(defaultCode);

//     // Clear console messages
//     editorLib.clearConsoleScreen();
// })

editorLib.init(codeEditor);


// function fileDisplay()
// {
//     var file = document.getElementById('multipleFiles');

//     for(var i=0; i<file.files.length; ++i)
//     {
//         var reader = new FileReader();

//         reader.onload = function(e)
//         {
//             codeEditor.setValue(e.target.result);
//             // console.log(e.target.result);
//         };

//         // To display the files with only pes 
//         let cur_file = file.files[i]
//         if(cur_file.name.match(/.*pes.*\.c$/i)){
//             addDestroyTabs();
//             reader.readAsBinaryString(cur_file);

//         }

//         // if(cur_file.name.match(/\.c$/i))
//         //     reader.readAsBinaryString(cur_file);

//     }
// }


// $.fn.fileDisplay = function(){

//     var file = document.getElementById('multipleFiles');

//     for(var i=0; i<file.files.length; ++i)
//     {
//         var reader = new FileReader();

//         reader.onload = function(e)
//         {
//             codeEditor.setValue(e.target.result);
//             // console.log(e.target.result);
//         };

//         // To display the files with only pes 
//         let cur_file = file.files[i]
//         if(cur_file.name.match(/.*pes.*\.c$/i)){
//             // addDestroyTabs();
//             reader.readAsBinaryString(cur_file);

//         }

//         // if(cur_file.name.match(/\.c$/i))
//         //     reader.readAsBinaryString(cur_file);

//     }
// }



function arrayMin(arr) {
  return arr.reduce(function (p, v) {
    return ( p < v ? p : v );
  });
}

function arrayMax(arr) {
  return arr.reduce(function (p, v) {
    return ( p > v ? p : v );
  });
}

function updateMarks(codeData){
	
	
	var output_list = codeData.split("\n");
	
	for(var i=0;i<output_list.length; ++i){
		if(output_list[i].match(/Your Total Score/i)){
			$("#compile-message").text(output_list[i]);
			break;
		}
	}

	$("#testcase-passed").text(output_list[0]);

}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// $.fn.highlighter = function(){
// // console.log(document.this.parent().attr("id"));
// 	console.log("hi");
// };

$.fn.addEditorTab = function(name, tabName, cur_file) {
	$('ul', this).append('<li ><a id="editor-tab-'+name+'" href="#tab-' + name + '">' + tabName + '</a><span class="ui-icon ui-icon-close" role="presentation"></li>');
	$(this).append("<div id='tab-" + name + "' class='editor__body'><div id='editor-" + name + "' class='editor__code'></div></div>");
	$(this).tabs("refresh");

	let codeEditor = ace.edit("editor-" + name);

	editorLib.init(codeEditor);

	var reader = new FileReader();

	reader.onload = function(e)
	{
	    codeEditor.setValue(e.target.result);
	    // console.log(e.target.result);
	};
	// var Range = ace.require('ace/range').Range;

	// codeEditor.session.addMarker(new Range(1, 12, 15, 12), "ace_active-line", "fullLine");

	reader.readAsBinaryString(cur_file);

	$(this).tabs({ active: 1 });

	return codeEditor;
};

$.fn.addMessages = function(name, cur_file, count,output_string) {

	$("#testcase-list").append('<li id="testcase-tab-'+name+'"><a href="#tab' + count+ '"> Test Case ' + count + '</a></li>');
	$("#testcase-tabs").append('<div class="testcase-main" id="tab'+count+'"><p class="message-header">Debugger Message</p><div class="message__console"><ul class="message__console-logs"><li><pre id="tab'+count+'-1">hello this is me</pre></li></ul></div><p class="message-header">Input</p><div class="message__console"><ul class="message__console-logs"><li><pre id="tab'+count+'-2">hello this is me</pre></li></ul></div><p class="message-header">Your Output</p><div class="message__console"><ul class="message__console-logs"><li><pre id="tab'+count+'-3">hello this is me</pre></li></ul></div><p class="message-header">Expected Output</p><div class="message__console"><ul class="message__console-logs"><li><pre id="tab'+count+'-4">hello this is me</pre></li></ul></div></div>');
	$(this).tabs("refresh");
	// function createError(obj){
 //    obj.addClass('ui-state-error ui-corner-all');
 //    obj.append('<span class="ui-icon ui-icon-alert" style="float: left;"></span>');
	// }
	// createError($("#testcase-tab1"));
	line_numbers[name] = [];

	var output_list = output_string.split("\n");

	var c = 0;

	var c1 = 0;

	var your_output = "";
	var expected_output = "";
	var compiler_message = "";
	var file_flag = 1;
	var while_flag = 0;
	var prev_line_int =0;

	for(var i=0; i < output_list.length; ++i){
		if(count == c){
			if(output_list[i].match(/Your Output:$/i)){
				c1 = 1;
			}

			else if(output_list[i].match(/Expected Output:$/i)){
				c1 = 2;
			}

			else if(output_list[i].match(/Debugger Message:$/i)){
				c1 = 3;
			}

			else if(output_list[i].match(/For test case/i)){
				break;
			}

			else if(c1 == 1){
				your_output += output_list[i]+"\n";
			}

			else if(c1 == 2){
				expected_output += output_list[i]+"\n";
			}

			else if(c1 == 3){
				compiler_message += output_list[i]+"\n";
				if(output_list[i].match(/^\d*\s.*/)){
					var val = parseInt(output_list[i].split('\t')[0]);
					var found = line_numbers[name].find(element => element == val)
					if(found){
						line_numbers[name] = [];
					}
					// if(output_list[i].match(output_list[i].match(/while/)) && prev_line_int){
						
					// 	while_flag = 1;
					// }
					// if(output_list[i].match(output_list[i].match(/}/)) && while_flag && prev_line_int){
					// 	line_numbers[name].push(val);
					// 	break;
					// }
					line_numbers[name].push(val);
					prev_line_int = 1;
				}
				else if(output_list[i].match(/\.c/i) && file_flag){
					var temp_list = output_list[i].split(' ');
					files_line_numbers[name] = temp_list[temp_list.length-1].split(':')[0];
					prev_line_int = 0;
					// console.log(temp_list[temp_list.length-1].split(':'));
				}
				else if(output_list[i].match(/^Local Varaibles:*/i)){
					file_flag = 0;
					prev_line_int = 0;
				}
				else{
					prev_line_int = 0;
				}
			}
		}
		else if(output_list[i].match(/For test case/)){
			++c;
			if(c > count) break;
		}
	}

	for(var i=1; i <= count; ++i){
		var temp = output_list[i].split(':');
		var marks = temp[1].split(' ')[1];
		// console.log(temp)
	}
	$("#testcase-tabs").tabs()
	console.log(count)
	if(marks === "0"){
		$('#testcase-tabs .ui-tabs-nav a[href="#tab' + count+ '"], #tab' + count + '').addClass('status1');
	}
	else{
		$('#testcase-tabs .ui-tabs-nav a[href="#tab' + count+ '"], #tab' + count + '').addClass('status2');
	}

	// console.log(line_numbers)
	// console.log(expected_output);
	// console.log(your_output);
	// console.log(compiler_message);

	var reader = new FileReader();

    reader.onload = function(e)
    {
        $("#tab"+count+"-1").text(compiler_message);
        $("#tab"+count+"-2").text(e.target.result);
        $("#tab"+count+"-3").text(your_output);
        $("#tab"+count+"-4").text(expected_output);
        // console.log(e.target.result);
    };

    // var Range = ace.require('ace/range').Range;

    // codeEditor.session.addMarker(new Range(1, 12, 15, 12), "ace_active-line", "fullLine");
  
    // reader.readAsBinaryString(cur_file);
	reader.readAsText(cur_file);
    $(this).tabs({ active: 1 });
};



$(function() {
    $("#temp-tab").hide();
    $("#code-compile-test-view").hide();
    $("#testcase-tabs").tabs().addClass( "ui-tabs-vertical ui-helper-clearfix" );
    // $( "#tabs li" ).removeClass( "ui-corner-top" ).addClass( "ui-corner-left" );
    $("#run_button").hide();
    $('#multifilesForm').submit(function() {
        $(this).hide();
        //$("#run_button").show();
        var file = document.getElementById('multipleFiles');
        // console.log(file.files)
        program_files = file.files;

        var tabs = $("#tabs").tabs();
        var index = 0;
    
        for(var i=0; i<file.files.length; ++i){

            let cur_file = file.files[i];

            var filePath = cur_file.name;
            var fileName = cur_file.name;
            if(fileName.match(/\.c$/i)){
                editors[filePath] = tabs.addEditorTab(filePath, fileName, cur_file);
            }
            else if(fileName.match(/\.h$/i)){
            	continue;
            }
            else{
            	text_files[index] = cur_file;
            	index++;
            }
            // window.location = "#tab-main.c"
        }
        //$("#run_button").show();

            // editors[file2Path] = tabs.addEditorTab(file2Path, file2Name, file2Contents);

        tabs.on("click", "span.ui-icon-close", function() {
        var panelId = $(this).closest("li").remove().attr("aria-controls");
        var editorId = panelId.replace("tab-", "editor-");

        console.log("A, Editor: " + editorId);
        $("div[id='" + editorId + "']").remove();

        console.log("B, Panel: " + panelId);
        $("div[id='" + panelId + "']").remove();

        console.log("C");
        editors[editorId.replace("editor-", "")].destroy();

        console.log("D");
        tabs.tabs("refresh");
        });

        sleep(1500).then(() => { $("#run_button").show(); });
        // $("#run_button").show();
    });

    $("#run_button").click(function(){
    	$("#run_button").hide();
    	$("#testcase-temp-tab").hide();
    	$("#code-compile-test-view").show();
	   	$.getJSON({
	        url: "/json_data_func",
	        success: function(data){
	        	updateMarks(data.a);
			}
		});

	    $("html, body").animate({
	        scrollTop: $('html, body').get(0).scrollHeight
	    }, 2000);

	    var output_tabs = $("#testcase-tabs").tabs();

	    editorLib.clearConsoleScreen();

	   	$.getJSON({
	        url: "/json_data_func",
	        success: function(data){
	            editorLib.printToConsole(data.a);
	            // output_string = data.a;
			    for(var i=0;i<text_files.length;++i){
			    	var cur_file = text_files[i];
			    	var fileName = cur_file.name;
			    	output_tabs.addMessages(fileName, cur_file, i+1,data.a);
			    	// console.log(text_files[i]);
			    }

			$("#testcase-list li a").click(function(){
				if(marker !== ""){
					editors[files_line_numbers[file_number_id]].session.removeMarker(marker);
				}
				// console.log($(this).parent().attr("id"))
	    		file_number_id = $(this).parent().attr("id").split('-')[2];
	    		if(line_numbers[file_number_id].length!=0){
		    		var min = arrayMin(line_numbers[file_number_id]);
		    		var max = arrayMax(line_numbers[file_number_id]);
		    		var Range = ace.require('ace/range').Range;
		    		// console.log(files_line_numbers);
		    		editors[files_line_numbers[file_number_id]].resize(true);
		    		editors[files_line_numbers[file_number_id]].gotoLine(min, 0, true);
		    		marker = editors[files_line_numbers[file_number_id]].session.addMarker(new Range(min-1, 0, max-1, 1), "myMarker", "fullLine");
	    		// console.log(marker)
	    		}
	    		else{
	    			marker = "";
	    		}
	   		});

			}
		});

    });

	//$("#testcase-list li a").each(function loopback(){
	// 		$(this).click(function(){
	// 			console.log("hello");
	// 		});
	// });

});

