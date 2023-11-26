function deleteRow() {
  var tableData = event.target.parentNode;
  var tableRow = tableData.parentNode;
  tableRow.parentNode.removeChild(tableRow);
}
function addRow() {
  // Get form values

  var classId = document.getElementById("classId").value;
  var className = document.getElementById("className").value;
  var startTime = document.getElementById("startTime").value;
  var duration = document.getElementById("duration").value;
  var daySelect = document.getElementById("daySelect");
  var location = document.getElementById("classLocation").value;
  var selectedDays = Array.from(daySelect.selectedOptions, (option) =>
    option.value.slice(0, 2)
  ).join(", ");

  // Calculate end time
  var startHour = parseInt(startTime.split(":")[0]);
  var startMinute = parseInt(startTime.split(":")[1]);
  var durationMinute = parseInt(duration);
  var durationHour = durationMinute / 60;
  durationMinute = durationMinute % 60;
  var endHour = startHour + durationHour;
  var endMinute = startMinute + durationMinute;
  if (endMinute >= 60) {
    endHour += 1;
    endMinute -= 60;
  }

  var endTime =
    endHour.toString().padStart(2, "0") +
    ":" +
    endMinute.toString().padStart(2, "0");
  var location = document.getElementById("classLocation").value;

  // Create a new row
  var table = document
    .getElementById("classTable")
    .getElementsByTagName("tbody")[0];
  var newRow = table.insertRow(table.rows.length);

  // Insert cells
  var cell1 = newRow.insertCell(0);
  var cell2 = newRow.insertCell(1);
  var cell3 = newRow.insertCell(2);
  var cell4 = newRow.insertCell(3);
  var cell5 = newRow.insertCell(4);
  var cell6 = newRow.insertCell(5);
  var cell7 = newRow.insertCell(6);
  var cell8 = newRow.insertCell(7);

  // Populate cells with form values
  cell1.innerHTML = classId;
  cell2.innerHTML = className;
  cell3.innerHTML = startTime;
  cell4.innerHTML = endTime;
  cell5.innerHTML = duration;
  cell6.innerHTML = selectedDays;
  cell7.innerHTML = location;
  cell8.innerHTML =
    '<button class="btn btn-danger" type="button" onclick="deleteRow()">Delete</button>';

  // Clear the form for the next entry
  document.getElementById("classForm").reset();
}

function Post() {
  var table = document.getElementById("classTable");
  var data = new Array();
  for (var i = 1; i < table.rows.length; i++) {
    data[i - 1] = new Array();
    c = 0;
    for (var j = 0; j < table.rows[i].cells.length - 1; j++) {
      if (j == 4) continue;
      if (j == 5) {
        data[i - 1][c] = table.rows[i].cells[j].innerHTML
          .split(",")
          .map((x) => x.trim().slice(0, 2));
      } else data[i - 1][c] = table.rows[i].cells[j].innerHTML;
      c++;
    }
  }
  //add maxDays and maxBreaks and maxCourses to data
  maxDays = document.getElementById("maxDays").value;
  maxBreaks = document.getElementById("maxBreaks").value;
  maxCourses = document.getElementById("maxCourses").value;

  if (maxDays != 0) data.push(["maxDays", maxDays]);
  if (maxBreaks != 0) data.push(["maxBreaks", maxBreaks]);
  if (maxCourses != 0) data.push(["maxCourses", maxCourses]);

  var json = JSON.stringify(data);

  // send json to server
  var request = new XMLHttpRequest();

  request.open("POST", "/schedule", true);
  request.setRequestHeader("Content-Type", "application/json");
  request.onreadystatechange = function () {
    if (request.readyState == 4 && request.status == 200) {
      var json = JSON.parse(request.responseText);

      var div = document.getElementById("solutionTables");
      if (document.getElementById("solutionTables") != null) {
        //delete all its children
        while (div.firstChild) {
          div.removeChild(div.firstChild);
        }
      }

      if (document.getElementById("solutionHeader") == null) {
        var h1 = document.createElement("h1");
        h1.setAttribute("id", "solutionHeader");
        h1.setAttribute("class", "display-4");
        h1.innerHTML = "Solutions";
        div.appendChild(h1);
      }
      json = json["data"];
      for (i = 0; i < json.length; i++) {
        var table = document.createElement("table");
        table.setAttribute("class", "table table-striped");
        var thead = document.createElement("thead");
        var tbody = document.createElement("tbody");
        var tr = document.createElement("tr");
        var th = document.createElement("th");
        th.setAttribute("scope", "col");
        th.innerHTML = "Class ID";
        tr.appendChild(th);
        th = document.createElement("th");
        th.setAttribute("scope", "col");
        th.innerHTML = "Class Name";
        tr.appendChild(th);
        th = document.createElement("th");
        th.setAttribute("scope", "col");
        th.innerHTML = "Start Time";
        tr.appendChild(th);
        th = document.createElement("th");
        th.setAttribute("scope", "col");
        th.innerHTML = "End Time";
        tr.appendChild(th);
        th = document.createElement("th");
        th.setAttribute("scope", "col");
        th.innerHTML = "Duration";
        tr.appendChild(th);
        th = document.createElement("th");
        th.setAttribute("scope", "col");
        th.innerHTML = "Days";
        tr.appendChild(th);
        th = document.createElement("th");
        th.setAttribute("scope", "col");
        th.innerHTML = "Location";
        tr.appendChild(th);
        thead.appendChild(tr);
        table.appendChild(thead);
        table.appendChild(tbody);
        div.appendChild(table);

        for (j = 0; j < json[i].length; j++) {
          var tr = document.createElement("tr");
          var td = document.createElement("td");
          td.innerHTML = json[i][j]["id"];
          tr.appendChild(td);
          td = document.createElement("td");
          td.innerHTML = json[i][j]["name"];
          tr.appendChild(td);
          td = document.createElement("td");
          //conver it to 00:00 format
          td.innerHTML =
            (json[i][j]["start_time"] / 60).toString().padStart(2, "0") +
            ":" +
            (json[i][j]["start_time"] % 60).toString().padStart(2, "0");
          tr.appendChild(td);
          td = document.createElement("td");
          td.innerHTML =
            (json[i][j]["end_time"] / 60).toString().padStart(2, "0") +
            ":" +
            (json[i][j]["end_time"] % 60).toString().padStart(2, "0");
          tr.appendChild(td);
          td = document.createElement("td");

          // claculate duration manually

          var duration =
            parseInt(json[i][j]["end_time"]) -
            parseInt(json[i][j]["start_time"]);
          td.innerHTML = duration;

          tr.appendChild(td);
          td = document.createElement("td");

          //days are numbers so we need to convert them to day Names
          var days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
          var daysNames = json[i][j]["days"].map((x) => days[x - 1]).join(", ");

          td.innerHTML = daysNames;
          tr.appendChild(td);
          td = document.createElement("td");
          td.innerHTML = json[i][j]["location"];
          tr.appendChild(td);
          tbody.appendChild(tr);
        }
      }
    }
  };
  request.send(json);
}
