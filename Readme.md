```javascript
function myFunction() {
  var parts=[];
  // Assuming last element of the argument is the one with 
  // individual expenseces shared.
  for (var part=0; part < arguments.length-1 && arguments[part][0] != ''; part++){
   parts.push(arguments[part][0].toString());
   }
  var data={};
  data['calc'] = []
  for (var by in parts){
     var dat = {
      'by':parts[by],
      'amount':parseFloat(arguments[by][arguments[by].length-1]),
      'participants':parts
    }
    data['calc'].push(dat);
  }
  var indi = arguments.length-1;
  for (var betwns=0; betwns <= arguments[indi].length-1; betwns++){
    var btwnparts = arguments[indi][betwns][2].split(',')
    //return typeof(arguments[indi][betwns][0]);
    if (arguments[indi][betwns][0] == '')
      break;
    var dat = {
      'by': arguments[indi][betwns][1].toString(),
      'amount': parseFloat(arguments[indi][betwns][0]),
      'participants': btwnparts,
    }
    data['calc'].push(dat);
  }
  var options = {
   'method' : 'post',
   'contentType': 'application/json',
   'payload' : JSON.stringify(data)
 };
 backdata = JSON.parse(UrlFetchApp.fetch('http://infinite-chamber-24921.herokuapp.com/', options).getContentText());
 var arr = [];
 
 // converting json data to table.
 // allparts is dict with name:number mactching.
 arr[0] = ['']
 var allparts = backdata['allparts']
 for (part in backdata['allparts'])
   arr[0][allparts[part]+1] = part
 for (var part in backdata['allparts']){
   var currnumber = allparts[part] +1;
   arr[currnumber]=[];
   arr[currnumber][0] = part;
   for (var part2 in backdata[part]) {
     arr[currnumber][allparts[part2]+1] = backdata[part][part2]
   }
 }
 return arr
}
```
