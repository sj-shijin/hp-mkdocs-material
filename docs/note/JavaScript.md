# JavaScript

## 1.JavaScript的使用

```html
<head>
    ...
    <script src="引入js文件路径" type="text/javascript" charset="uft-8"></script>
</head>
<body>
    ...
    <script>
        //写在body的最后，保证页面加载完成再运行js代码
    </script>
</body>
```

## 2.快速入门

### 2.1.基础语法

```javascript
//严格模式（使代码更加规范）
"use strict"; //添加在脚本或函数的第一行

//Number数字
    var f = 3.14; //全局变量（在函数内定义的为局部变量），
    let i = 1001; //局部，块级变量
    const s = 123e5;//常量
//String字符串
    var s1 = 'str';
    var s2 = "str";
//相等==与绝对相对===
    16 == '16' //true 相等只要满足值相等
    16 === '16' //false 绝对相等要满足值和数据类型均相等
    NaN === NaN //false NaN与所有值都不相等
    isNaN(NaN) //true
//Undefined未定义
    var x; // x 为undefined
//Null空，定义为空对象
    var x = null;
    null == undefined //true
    null === undefined //false
//与或非
    && || !
//条件运算符
    (condition) ? valuetrue : valuefalse;
//类型转换
    Number(value)
    String(value)
    Boolean(value)
    xxx.toString() //常用于输出时
//Array数组
    var a1 = [1,2,3,'abc'];
    var a2 = new Array(1,2,3,'afd');
//在HTML中，的全局变量为window对象，所有数据变量都属于window对象
```

### 2.2.基础语句

```javascript
//条件语句
    if (condition1) {
        ...
    } else if (condition2) {
        ...
    } else {
        ...
    };
//循环语句1
    for (let i = 0; i < max; i++) {
        ...
    }
//循环语句2
    for (const key in object) {
        ...
    }
//循环语句3
    for (const value of object) {
        ...
    }
//循环语句4
    while (condition) {
        ...
    }
//循环语句5
    do {
        ...
    } while (condition);
```

### 2.3.JavaScript对象

```javascript
//Object对象
    var o = {
        name:'sj',
        'name':'shijin', //与上一项key视为相同，会覆盖上一个的值
        age:19
        f : function (x,y) {
            return x + y;
        }
    };
//两种访问方式（可动态添加属性）
    o.name;
    o["name"];
```

### 2.4.JavaScript函数

```javascript
//function函数
    function f(x,y) {
        return x + y;
    }
//匿名函数
    const f = function (x,y) {
        return x + y;
    }
//ES6箭头函数
    const f = (x,y) => x + y;
    const f = (x,y) => { return x + y; }
//JS对函数的传入参数个数没有强制性要求
    function f(x,y) {
        arguments === [1,2,3,4,5] //一个iterator，存有所有参数
    }
    f(1,2,3,4,5)
    function f2(x,y,...rest) {
        rest === [3,4,5] //一个数组，存有剩余参数
    }
    f2(1,2,3,4,5)
```

### 2.5.JSON字符串与JavaScript对象

```javascript
//JSON是一种传输数据的格式
obj = JSON.parse(jsonstr); //JSON字符串转为JS对象
str = JSON.stringify(obj); //JS对象转为JSON字符串
```

## 3.apply函数和call函数

```javascript
var person = {
  fullName: function(city, country) {
    return this.firstName + " " + this.lastName + "," + city + "," + country;
  }
}
var person1 = {
  firstName:"John",
  lastName: "Doe"
}
person.fullName.apply(person1, ["Oslo", "Norway"]);
person.fullName.call(person1, "Oslo", "Norway");
//可以将person中的方法用于person1中（改变this的指向）
```

## 4.Date(日期)对象

```javascript
var today = new Date();
var d1 = new Date(dateString);
var d2 = new Date(value); //通过1970年1月1日至今的毫秒数生成日期
var d3 = new Date(year,monthIndex,day,hours,mintes,seconds,milliseconds) //至少前两个参数
d1.getTime() //返回1970年1月1日至今的毫秒数
d1.getFullYear() //年
d1.getMonth() //月 0~11
d1.getDate() //日
d1.getDay() //星期
```

## 5.HTML DOM

```javascript
//获取cookie
document.cookie
//查找节点
var x = document.getElementById("id001"); //通过id查找，返回节点
var y = x.getElementsByTagName("p"); //通过标签名查找（p标签），返回HTMLCollection
var z = document.getElementsByClassName('class1'); //通过类名查找，返回HTMLCollection
    //document代表整个页面的根节点
//修改节点
    //修改标签内容
    x.innerText = "文本内容";
    x.innerHTML = "HTML内容";
    //修改标签属性
    x.className = "newclassname";
    x.setAttribute('class','newclassname');
    //修改标签的css-style
    x.style.color = "red";
//新增节点
    //移动已存在的节点
    father.appendChild(x); //将查找到的x节点移动到father节点的最后
    //新建节点
    var nx = document.createElement('p'); //创建p标签
    nx.id = 'p1';
    nx.innerText = 'Hello'; //设置属性和内容
    father.appendChild(nx); //将新节点nx新增到father节点的最后
    father.insertBefore(nx,childx) //将新节点nx插入到father节点的子节点childx前
    father.replaceChild(nx,childx) //替换
//删除节点（找到父节点，调用父节点的方法删除该节点）
    xfather = x.parentElement;
    x.parentElement.removeChild(x);
    xfather.children //删除节点时会实时更新子节点
```

```javascript
//获得和设置表单的值，假设x为一个input节点
    x.value
    x.value = '123' //type = 'text'
    x.checked
    x.checked = true //type = 'radio'
```

```html
<button html事件='javascript 代码'></button> <!--一般js代码为调用函数-->
<button onclick="javascript 代码"></button>
<!--
常用HTML事件
改变元素onchange
点击元素onclick
在元素上移动鼠标onmouseover
在元素上移开鼠标onmouseout
按下键盘按键onkeydown
完成加载onload
-->
<button onclick="return judge()"></button> <!--若judge函数返回false，则该按钮不会被执行-->
```

## 6.HTML BOM

```javascript
//弹出窗口
window.alert(text)
//窗口的文档显示区域的宽高
window.innerWidth
window.innerHeight
//窗口的外部宽高，包含工具条与滚动条
window.outerWidth
window.outerHeight
//浏览器的user-agent值
nevigator.userAgent
//加载前一个URL
history.back()
//加载后一个URL
history.forward()
```

## 7.JQuery

JQuery库中包含大量JS函数，简化语法。

[jQuery API 中文在线手册](http://jquery.cuishifeng.cn)

### 7.1JQuery的使用

```html
<head>
    ...
    <script src="jquery.js的url"></script>
</head>
```

### 7.2JQuery语法

```javascript
$(selector).action()
//selector就是css的选择器

//页面载入
$(document).ready(function(){
    ...
})
//等价于
$(function(){
    ...
})

//节点文本操作
$('#id001').text("文本内容");
$('#id001').html("<strong>123</strong>");
//css操作
$('#id002').css('color','red');
$('#id002').css({'color':'red','font-size':20px});
//显示隐藏
$('#id003').show();
$('#')
```

### 7.3JQuery事件

```javascript
$('#id').mousemove(function(e){
    ... //e中可读取页面相关数据
})
//可查阅中文在线手册
```
