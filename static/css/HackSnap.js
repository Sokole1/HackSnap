var groupValue = document.getElementById("groupDropDown");
var subjectDropArea = document.getElementById("subjectArea");

function checkSubjGroup(){
    console.log(document.getElementById("groupDropDown").value);
    switch(document.getElementById("groupDropDown").value){
        case "Group 1 - Studies in Language and Literature":
            document.getElementById("subjectDropDown").innerHTML="<option value='English'>English</option>"
            break;
        case "Group 2 - Language Acquisition":
            document.getElementById("subjectDropDown").innerHTML="<option value='spanish'>Spanish</option><option value='french'>French</option><option value='mandarin'>Mandarin</option><option value='japanese'>Japanese</option>"
            break;
        case "Group 3 - Individuals and Societies":
            document.getElementById("subjectDropDown").innerHTML="<option value='buisness'>Buisness</option><option value='itgs'>ITGS</option><option value='geography'>Geography</option><option value='history'>History</option>"
            break;
        case "Group 4 - Experimental Sciences":
            document.getElementById("subjectDropDown").innerHTML="<option value='physics'>Physics</option><option value='biology'>Biology</option><option value='chemistry'>Chemistry</option>"
            break;
        case "Group 5 - Mathematics":
            document.getElementById("subjectDropDown").innerHTML="<option value='math'>Math</option>"
            break;
        case "Group 6 - The Arts":
            document.getElementById("subjectDropDown").innerHTML="<option value='music'>Music</option>"
            break;
        default:
            console.log("no Option")
    }
}

