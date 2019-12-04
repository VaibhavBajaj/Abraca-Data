function getData(elementId) {
    var data = document.getElementById(elementId).value;
    if (data === "text here") {
        data = null;
    }
    return data;
}

function insertFunction() {
    var data = {};
    data["name"] = getData("insert_name");
    data["affiliation"] = getData("insert_affiliation");
    data["citedby"] = getData("insert_citedby");
    data["pub_title"] = getData("insert_pub_title");
    data["pub_year"] = getData("insert_pub_year");
    data["pub_url"] = getData("insert_pub_url");
    data["journal"] = getData("insert_journal");
    $.post( "/insert", { "data" : data }).done(function(status) {
        var code = status["code"];
        if(code === 0) {
            alert("Article successfully inserted");
        } else {
          alert("Error code: " + stat);
        }
    });
}

function deleteFunction() {
    alert("Here");
    var data = {};
    data["id"] = getData("delete_id");
    $.post( "/delete", { "data" : data }).done(function(status) {
        var code = status["code"];
        if(code === 0) {
            alert("Article successfully deleted");
        } else {
            alert("Error code: " + stat);
        }
    });
}