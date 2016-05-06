
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
    document.getElementById("calendar-month-year").innerHTML = month_name[month]+" "+year;
    document.getElementById("calendar-dates").appendChild(calendar);
    var meetinginfo="";


}

function get_calendar(day_no, days, day_name){
    var table = document.createElement('table');
    var tr = document.createElement('tr');

    //row for the days of the week
    for(var c=0; c<=6; c++){
        var td = document.createElement('td');
        td.innerHTML = day_name[c].toUpperCase();
        td.style.borderBottom="thin solid #586F7C";
        td.style.verticalAlign="bottom";
        //td.style.marginBottom="5px";
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
        if(count == (new Date()).getDate()){
            td.style.color="#CF5C36";
        }
        if(count==2){ //.................................ADD ICON TO DATE HEREEEEE!!
            var trr = document.createElement('trr');
            trr.innerHTML=count+"<br>";
            var img = document.createElement('img');
            img.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/pin-24.png';
            img.id="img";
            img.type="button";
            img.onclick=function(){alert("You've got a meeting!")};
            meetinginfo="meeting on may 2";

            td.appendChild(trr);
            td.appendChild(img);
        }
        else{
            td.innerHTML=count;
        }
        /*td.innerHTML = count;*/
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
            td.style.backgroundColor="#F5F1ED";

            if(count == (new Date()).getDate()){
                var a = document.createElement('a');
                td.style.color="#CF5C36";
                td.style.backgroundColor="#CF5C36";
            }

              if(count<=31){td.innerHTML = count;} //adding extra days

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
function test(){
    alert("test");
}

function produceMessage(){
    return meetinginfo;
    //alert(meetinginfo);
}


