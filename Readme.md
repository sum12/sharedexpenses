```javascript
function myFunction() {
  var parts=[];
  for (var part in arguments)
   parts.push(arguments[part][0].toString());
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
  var options = {
   'method' : 'post',
   'contentType': 'application/json',
   'payload' : JSON.stringify(data)
 };
 backdata = JSON.parse(UrlFetchApp.fetch('http://infinite-chamber-24921.herokuapp.com/', options).getContentText());
 var arr = [];
 
 
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
