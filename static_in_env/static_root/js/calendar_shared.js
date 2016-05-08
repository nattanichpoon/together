
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
    var shared_calendar = get_calendar(day_no, days, day_name);
    var members = get_members();
    var monthyear = document.createTextNode(month_name[month]+" "+year);

    document.getElementById("shared-calendar-dates").appendChild(shared_calendar);
    document.getElementById("memberinfo-title").innerHTML = "Member List";
    document.getElementById("memberinfo-body").appendChild(members);

    var prev = document.createElement("BUTTON");
    prev.style.backgroundColor="#586F7C";
    prev.style.color="#f5f1ed";
    prev.style.borderStyle='none';
    var prevt = document.createTextNode("<");
    prev.appendChild(prevt);
    document.getElementById('shared-calendar-month-year').appendChild(prev);
    prev.onclick=function(){
       alert('previous');
    }

    document.getElementById('shared-calendar-month-year').appendChild(monthyear);

    var next = document.createElement("BUTTON");
    next.style.backgroundColor="#586F7C";
    next.style.color="#f5f1ed";
    next.style.borderStyle='none';
    var nextt = document.createTextNode(">");
    next.appendChild(nextt);
    document.getElementById('shared-calendar-month-year').appendChild(next);


}

function get_calendar(day_no, days, day_name){

    //red
    var icon1 = document.createElement('img');
    icon1.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/star-24.png';
     //blue
    var icon2 = document.createElement('img');
    icon2.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/pencil-24.png';
    //orange
    var icon3 = document.createElement('img');
    icon3.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/running-24.png';
    //green
    var icon4 = document.createElement('img');
    icon4.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/bike-24.png';
    //yellow
    var icon5 = document.createElement('img');
    icon5.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/microphone-24.png';
    //beige
    var icon6 = document.createElement('img');
    icon6.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/car-24.png';
   //blue
    var icon7 = document.createElement('img');
    icon7.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/hotair-24.png';
    //green
    var icon8 = document.createElement('img');
    icon8.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/motorcycle-24.png';
    //navy
    var icon9 = document.createElement('img');
    icon9.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/plane-24.png';
    //beige
    var icon10 = document.createElement('img');
    icon10.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/rainbow-24.png';


    var table = document.createElement('table');
    //table.style.backgroundColor="#d89d47";
    var tr = document.createElement('tr');
    //tr.style.backgroundColor="#ffffff";

    //row for the days of the week
    for(var c=0; c<=6; c++){
        var td = document.createElement('td');
        td.innerHTML = day_name[c].toUpperCase();
        td.style.borderBottom="thin solid #f5f1ed";
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
            td.appendChild(icon1);
            td.appendChild(icon2);
            td.onclick=function(){//nothing yet
            };

        }else if(count==5){ //.................................ADD ICON TO DATE HEREEEEE!!

            td.appendChild(icon2);
            td.onclick=function(){//nothing yet
            };
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

function get_members(){

    var membercount=5;
    //icons
    //red
    var icon1 = document.createElement('img');
    icon1.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/star-24.png';
     //blue
    var icon2 = document.createElement('img');
    icon2.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/pencil-24.png';
    //orange
    var icon3 = document.createElement('img');
    icon3.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/running-24.png';
    //green
    var icon4 = document.createElement('img');
    icon4.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/bike-24.png';
    //yellow
    var icon5 = document.createElement('img');
    icon5.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/microphone-24.png';
    //beige
    var icon6 = document.createElement('img');
    icon6.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/car-24.png';
   //blue
    var icon7 = document.createElement('img');
    icon7.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/hotair-24.png';
    //green
    var icon8 = document.createElement('img');
    icon8.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/motorcycle-24.png';
    //navy
    var icon9 = document.createElement('img');
    icon9.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/plane-24.png';
    //beige
    var icon10 = document.createElement('img');
    icon10.src='https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/rainbow-24.png';



    var table = document.createElement('table');

    /*for(var i=1; i<=3; i++){
        var tr = document.createElement('tr');
        var td1 = document.createElement('td');
        td1.appendChild(icon1);
        var td2 = document.createElement('td');
        td2.innerHTML='&nbsp;&nbsp;&nbsp;Member'+i;
        tr.appendChild(td1);
        tr.appendChild(td2);
        table.appendChild(tr);
    }*/

    var tr1 = document.createElement('tr');
    var td11 = document.createElement('td');
    td11.style.padding='10px';
    td11.appendChild(icon1);
    var td12 = document.createElement('td');
    td12.style.padding='10px';
    td12.innerHTML='&nbsp;&nbsp;&nbsp;Member1';
    tr1.appendChild(td11);
    tr1.appendChild(td12);
    table.appendChild(tr1);

    var tr2 = document.createElement('tr');
    var td21 = document.createElement('td');
    td21.style.padding='10px';
    td21.appendChild(icon2);
    var td22 = document.createElement('td');
    td22.style.padding='10px';
    td22.innerHTML='&nbsp;&nbsp;&nbsp;Member2';
    tr2.appendChild(td21);
    tr2.appendChild(td22);
    table.appendChild(tr2);

    var tr3 = document.createElement('tr');
    var td31 = document.createElement('td');
    td31.style.padding='10px';
    td31.appendChild(icon3);
    var td32 = document.createElement('td');
    td32.style.padding='10px';
    td32.innerHTML='&nbsp;&nbsp;&nbsp;Member3';
    tr3.appendChild(td31);
    tr3.appendChild(td32);
    table.appendChild(tr3);





    return table;
}



