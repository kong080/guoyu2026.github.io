const fs=require('fs');
const VM=require('vm');
let t=fs.readFileSync('index.html','utf-8');
const start=t.indexOf('<script>');
const end=t.indexOf('</script>');
const js=t.slice(start+8, end);
// 提取 DATA 行看它是否是对称的
const line=js.split('\n')[0]; // const DATA = ...
console.log('DATA行长度:', line.length, '首尾:', line.slice(0,15),'...',line.slice(-12));
try{
  new VM.Script(js,{filename:'app.js'});
  console.log('JS 语法 OK');
}catch(e){
  console.log('JS 语法错误:', e.message);
}