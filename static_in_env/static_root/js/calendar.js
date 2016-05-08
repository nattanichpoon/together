
window.onload = function(){
    var d = new Date();
    var n = d.getDate();
    // window.alert(n);
    var month_name = ['January','February','March','April','May','June','July','August','September','October','November','December'];
    var month = d.getMonth();   //0-11
    var year = d.getFullYear(); //2014
    var first_date = month_name[month] + " " + 1 + " " + year;
    //September 1 2014
    var tmp = new Date(first_date).toDateString();
    //Mon Sep 01 2014 ...
    var first_day = tmp.substring(0, 3);    //Mon
    var day_name = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
    var day_no = day_name.indexOf(first_day);   //1
    var days = new Date(year, month+1, 0).getDate();    //30
    //Tue Sep 30 2014 ...
    var calendar = get_calendar(day_no, days, day_name);
    var meetings = get_meetings();
    document.getElementById("calendar-month-year").innerHTML = month_name[month]+" "+year;
    document.getElementById("calendar-dates").appendChild(calendar);
    document.getElementById("meetinginfo-title").innerHTML = "Meeting Information";
    document.getElementById("meetinginfo-body").appendChild(meetings);

}

function get_calendar(day_no, days, day_name){
    var table = document.createElement('table');
    //table.style.backgroundColor="#d89d47";
    var tr = document.createElement('tr');
    //tr.style.backgroundColor="#ffffff";

    //row for the days of the week
    for(var c=0; c<=6; c++){
        var td = document.createElement('td');
        td.innerHTML = day_name[c].toUpperCase();
        td.style.borderBottom="thin solid #586F7C";
        td.style.verticalAlign="bottom";
        td.style.backgroundColor='#f5f1ed';
        tr.appendChild(td);

    }
    table.appendChild(tr);
    //tr.style.height='30px';
    //tr.style.width='220px'


    //create 2nd row
    tr = document.createElement('tr');
    var c;
    for(c=0; c<=6; c++){
        if(c == day_no){
            break;
        }
        var td = document.createElement('td');
        td.style.backgroundColor='#f5f1ed';
        td.innerHTML = "";
        /*var img = document.createElement('img');
        img.src='img/staricon.png'
        /*tr.appendChild(td);*/

        if(c==0){
            var trr = document.createElement('trr');
            trr.innerHTML="test<br>";
            var img = document.createElement('img');
            img.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/pin-24.png';
            /*trr.appendChild(img);*/
            td.appendChild(trr);
            td.appendChild(img);

        }
        tr.appendChild(td);


    }

    var count = 1;
    for(; c<=6; c++){
        var td = document.createElement('td');
        td.id='date_'+count;
        td.style.backgroundColor='#f5f1ed';
        td.innerHTML=count+'<br>';
        td.type='button';
        td.onmouseover=function(){this.style.backgroundColor='#C5DBE8'};
        td.onmouseout=function(){this.style.backgroundColor='#f5f1ed'};

        if(count == (new Date()).getDate()){
            td.style.color="red";
        }

        if(count==2){ //.................................ADD ICON TO DATE HEREEEEE!!
            var img = document.createElement('img');
            img.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/pin-24.png';
            td.appendChild(img);
            td.onclick=function(){document.getElementById("right").innerHTML =
                "<br><u>Meetings for May 2, 2012</u><br><br>" +
                "<li>Weekly group meeting" + "<ul>Project: A</ul><ul>Time: 10:30 AM</ul>" +
                "<li>Something else" + "<ul>Project: Annoying Thing</ul><ul>Time: 13:00 AM</ul><br>"};
        }else if(count==5){ //.................................ADD ICON TO DATE HEREEEEE!!
            var img = document.createElement('img');
            img.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/pin-24.png';
            td.appendChild(img);
            td.onclick=function(){document.getElementById("right").innerHTML =
                "<br><u>Meetings for May 5, 2012</u><br><br>" +
                "<li>Project Progress" + "<ul>Project: Something Else</ul><ul>Time: 9:00 AM</ul>" +
                "<li>Another Thing" + "<ul>Project: Together</ul><ul>Time: 12:30 AM</ul><br>"};
        }

        count++;
        tr.appendChild(td);
    }
    table.appendChild(tr);
    //tr.style.height='90px';
    //tr.style.width='220px';

    //rest of the date rows
    for(var r=3; r<=7; r++){
        tr = document.createElement('tr');
        for(var c=0; c<=6; c++){
            //var newday = days+4;
            if(count > days+4){
                table.appendChild(tr);
                return table;
            }


            var td = document.createElement('td');
            td.style.backgroundColor='#f5f1ed';

            td.type='button';
            td.onmouseover=function(){this.style.backgroundColor='#C5DBE8'};
            td.onmouseout=function(){this.style.backgroundColor='#f5f1ed'};

            if(count == (new Date()).getDate()){
                var a = document.createElement('a');
                td.style.color="red";
            }

              if(count<=31){td.innerHTML = count+'<br>';} //adding extra days

            count++;
            tr.appendChild(td);
        }

        tr.appendChild(td);

        table.appendChild(tr);
        tr.style.height='90px';
        tr.style.width='220px';
    }
    return table;
}

function get_meetings(){
    var table = document.createElement('table');

    var tr = document.createElement('tr');

        var td = document.createElement('td');
        td.id='right';

        td.style.verticalAlign="bottom";
        tr.appendChild(td);

    table.appendChild(tr);


    return table;
}

function test(){
    alert("test");
}

function produceMessage(){
    //document.write('10');
    //return "hello";
    alert(meetinginfo);
}