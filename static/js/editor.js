// Retrieve Elements
const consoleLogList = document.querySelector('.editor__console-logs');
const executeCodeBtn = document.querySelector('.editor__run');
const resetCodeBtn = document.querySelector('.editor__reset');

// Setup Ace
let codeEditor = ace.edit("editorCode");
let defaultCode = '#include <stdio.h> \r#include <stdlib.h>\r\rint main(){\r //Write your code here \r}';

let program_files;
var editors = {};


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
executeCodeBtn.addEventListener('click', () => {
    // Clear console messages
    editorLib.clearConsoleScreen();
    console.log(program_files)
    console.log(editors)

    // for(var i=0; i< program_files.length; ++i){
    //     // try{
    //         console.log(editors[program_files[i]].getValue())
    //     // }
    //     // catch{
            
    //     // }
    // }
    // Get input from the code editor
    // const userCode = codeEditor.getValue();
    $.getJSON({
        url: "/json_data_func",
        success: function(data){
            editorLib.printToConsole(data.a);
            console.log(data.a);
        }
    });
    
    // Run the user code
    // try {
    //     // Print to the console
    //     editorLib.printToConsole(userCode);
    // } catch (err) {
    //     console.error(err);
    // }
});

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

$.fn.addEditorTab = function(name, tabName, cur_file) {
  $('ul', this).append('<li><a href="#tab-' + name + '">' + tabName + '</a><span class="ui-icon ui-icon-close" role="presentation"></li>');
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

  return codeEditor;
};

$(function() {
    $("#temp-tab").hide();
    $('#multifilesForm').submit(function() {
        $(this).hide();
        var file = document.getElementById('multipleFiles');
        // console.log(file.files)
        program_files = file.files;

        var tabs = $("#tabs").tabs();
    
        for(var i=0; i<file.files.length; ++i){

            let cur_file = file.files[i];

            var filePath = cur_file.name;
            var fileName = cur_file.name;
            if(fileName.match(/\.c$/i)){
                editors[filePath] = tabs.addEditorTab(filePath, fileName, cur_file);
            }
            // window.location = "#tab-main.c"
        }

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
    });
});

