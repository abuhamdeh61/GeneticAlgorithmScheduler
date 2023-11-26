function load() {
  //make maxDays, maxBreaks, maxCourses default
  document.getElementById("maxDays").value = 3;
  document.getElementById("maxBreaks").value = 60;
  document.getElementById("maxCourses").value = 6;
  var table = document
    .getElementById("classTable")
    .getElementsByTagName("tbody")[0];

  data = [
    [
      "20565",
      "Class 763501",
      "13:00",
      "14:00",
      "60",
      ["MON", "WEN"],
      "On Campus",
    ],
    [
      "2548",
      "Class 561181",
      "16:00",
      "17:00",
      "60",
      ["SUN", "TUE", "THU"],
      "On Campus",
    ],
    [
      "62736",
      "Class 101121",
      "09:00",
      "10:00",
      "60",
      ["MON", "WEN"],
      "On Campus",
    ],

    ["25807", "Class 159661", "18:00", "19:00", "60", ["MON", "WEN"], "Online"],
    [
      "35907",
      "Class 92861",
      "11:00",
      "12:00",
      "60",
      ["SUN", "TUE", "THU"],
      "Online",
    ],
    [
      "95727",
      "Class 814411",
      "15:00",
      "16:00",
      "60",
      ["SUN", "TUE", "THU"],
      "On Campus",
    ],
    ["77029", "Class 848181", "13:00", "14:00", "60", ["MON", "WEN"], "Online"],
    ["33886", "Class 41981", "15:00", "16:00", "60", ["MON", "THU"], "Online"],
    [
      "50665",
      "Class 556371",
      "12:00",
      "13:00",
      "60",
      ["SUN", "TUE", "THU"],
      "Online",
    ],
    [
      "18796",
      "Class 886041",
      "10:00",
      "11:00",
      "60",
      ["SUN", "TUE", "THU"],
      "Online",
    ],
    [
      "96534",
      "Class 97631",
      "17:00",
      "18:00",
      "60",
      ["SUN", "TUE", "THU"],
      "On Campus",
    ],
    [
      "19086",
      "Class 219241",
      "18:00",
      "19:00",
      "60",
      ["SUN", "TUE", "THU"],
      "On Campus",
    ],
    [
      "22973",
      "Class 564201",
      "17:00",
      "18:00",
      "60",
      ["SUN", "TUE", "THU"],
      "On Campus",
    ],
    [
      "26916",
      "Class 873291",
      "09:00",
      "10:00",
      "60",
      ["SUN", "TUE", "THU"],
      "Online",
    ],
    [
      "73549",
      "Class 75571",
      "09:00",
      "10:00",
      "60",
      ["MON", "WEN"],
      "On Campus",
    ],
    [
      "75552",
      "Class 365531",
      "08:00",
      "09:00",
      "60",
      ["SUN", "TUE", "THU"],
      "On Campus",
    ],
    [
      "68653",
      "Class 401551",
      "11:00",
      "12:00",
      "60",
      ["SUN", "TUE", "THU"],
      "Online",
    ],
    [
      "76797",
      "Class 541211",
      "13:00",
      "14:00",
      "60",
      ["SUN", "TUE", "THU"],
      "Online",
    ],
    [
      "61755",
      "Class 947501",
      "18:00",
      "19:00",
      "60",
      ["SUN", "TUE", "THU"],
      "On Campus",
    ],
    [
      "36897",
      "Class 413061",
      "12:00",
      "13:00",
      "60",
      ["SUN", "TUE", "THU"],
      "On Campus",
    ],
    [
      "54490",
      "Class 317051",
      "15:00",
      "16:00",
      "60",
      ["SUN", "TUE", "THU"],
      "Online",
    ],
    ["44964", "Class 208751", "18:00", "19:00", "60", ["MON", "WEN"], "Online"],
    [
      "59180",
      "Class 35101",
      "17:00",
      "18:00",
      "60",
      ["SUN", "TUE", "THU"],
      "Online",
    ],
    [
      "38969",
      "Class 518731",
      "09:00",
      "10:00",
      "60",
      ["MON", "THU"],
      "On Campus",
    ],
    [
      "5619",
      "Class 47031",
      "08:00",
      "09:00",
      "60",
      ["SUN", "TUE", "THU"],
      "Online",
    ],
    [
      "85390",
      "Class 452911",
      "13:00",
      "14:00",
      "60",
      ["SUN", "TUE", "THU"],
      "On Campus",
    ],
    [
      "15062",
      "Class 111201",
      "13:00",
      "14:00",
      "60",
      ["SUN", "TUE", "THU"],
      "Online",
    ],
    [
      "71992",
      "Class 53011",
      "13:00",
      "14:00",
      "60",
      ["SUN", "TUE", "THU"],
      "Online",
    ],
    ["56401", "Class 331601", "18:00", "19:00", "60", ["MON", "WEN"], "Online"],
    ["74830", "Class 400741", "13:00", "14:00", "60", ["MON", "WEN"], "Online"],
  ];

  for (var i = 0; i < data.length; i++) {
    var newRow = table.insertRow(table.rows.length);

    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);
    var cell3 = newRow.insertCell(2);
    var cell4 = newRow.insertCell(3);
    var cell5 = newRow.insertCell(4);
    var cell6 = newRow.insertCell(5);
    var cell7 = newRow.insertCell(6);
    var cell8 = newRow.insertCell(7);

    cell1.innerHTML = data[i][0];
    cell2.innerHTML = data[i][1];
    cell3.innerHTML = data[i][2];
    cell4.innerHTML = data[i][3];
    cell5.innerHTML = data[i][4];
    cell6.innerHTML = data[i][5];
    cell7.innerHTML = data[i][6];

    cell8.innerHTML =
      '<button class="btn btn-danger" type="button" onclick="deleteRow()">Delete</button>';
  }
}
