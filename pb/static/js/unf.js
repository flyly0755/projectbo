function splitstr(varf)
         {
            //if (varf.indexOf("&") > -1)
            if($.inArray("&", varf)){
                var arr= new Array();
                //arr=(varf||"").split("&");
                //arr=(varf).split("&amp;");
                arr=(varf).split("&amp;");
                return arr;
                }
            else return 0;
         }

function shiftstr(varf)
    {
        splitstr(varf);
        return varf.shift();
    }