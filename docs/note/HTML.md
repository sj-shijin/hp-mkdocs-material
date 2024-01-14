# HTML

## 1.基础语法（默认模板）

```html
<!DOCTYPE html> <!-- html5 版本声明-->
<head>
    <meta charset="UTF-8">
    <title>页面标题</title>
    <link rel="stylesheet" href="引入css文件路径">
    <script src="引入js文件路径" type="text/javascript" charset="uft-8"></script>
</head>
<!--
    body标签
        bgcolor 背景颜色 
        text 字体颜色
-->
<body bgcolor="pink" text="blue">
    hello world
</body>
</html>
```

## 2.标题/水平线/段落/换行

```html
<!--
    标题标签<h1></h1>~<h6></h6> 从大到小
        不建议使用多个h1标签，h1标签会被搜索引擎获取，可能进入黑名单。
    水平线标签<hr> 块级元素
        width 宽度 1.百分比 2.px
        align 对齐方式 left/right/center(default)
        size 水平线粗细
    段落标签<p></p> 块级元素
        align 对齐方式 left(default)/right/center/justify(两端对齐)
    换行标签<br>
-->
<body>
    <h1>hello world</h1>
    <h2>hello world</h2>
    <hr width="50%" align="left" size="5">
    <hr width="500px" align="right" size="10">
    <p>
        内容
    </p>
    不自<!--此处会生成一个空格但不换行-->
    动换行<br>
    手动换行
</body>
```

## 3.列表

```html
<!--
    无序列表
        <ul>
            <li></li>
            ...
            <li></li>
        </ul>
        type 列表的图标 square(实心方块)/circle(空心圆)/disc(实心圆)(default)
    无序列表
        <ol>
            <li></li>
            ...
            <li></li>
        </ol>
        type 列表的图标 1(数字)(default)/a(小写字母)/A(大写字母)/i(小写罗马字母)/I(大写罗马字母)
-->
<body>
    <ul type="square">
        <li>张三</li>
        <li>李四</li>
        <li>王五</li>
    </ul>
    <ol type="a">
        <li>张三</li>
        <li>李四</li>
        <li>王五</li>
    </ol>
</body>
```

## 4.div和span

```html
<!--
    div标签<div></div> 块级元素；会自动换行；常用于布局；常配合css一起使用
        align 对齐方式（div中内容）left(default)/right/center/justify(两端对齐)
        height 高度
        line-height 行j=height时内容纵向居中
    span标签<span></span> 行内元素；不会自动换行；常配合css一起使用
-->
<body>
    <div align="center">
        内容
    </div>
    <span>内容</span>
</body>
```

## 5.格式化标签

```html
<!--
    字体标签<font></font> 行内元素
        color 字体颜色
        size 字体大小（1~7）
        face 字体风格
    pre标签<pre></pre> 块级元素 定义预格式化的文本。完全保留文本中的空格、制表、换行符。
    粗体标签<b></b>或<strong></strong> 行内元素
    斜体标签<i></i> 行内元素
    下划线标签<u></u> 行内元素
    删除线标签<del></del> 行内元素
    下标<sub></sub> 行内元素
    上标<sup></sup> 行内元素
-->
<body>
    <font color="red" size="5" face="楷体">你好</font>
    <pre>
    hello world
    helllllo   worrrrrld
    </pre>
    <b>粗体</b><strong>粗体2</strong>
    <i>斜体</i>
    <u>下划线</u>
    <del>删除线</del>
    <sub>下标</sub>
    <sup>上标</sup>
</body>
```

## 6.a标签（超链接/锚点）

```html
<!--
    a标签<a></a> 超链接；行内元素
        href="绝对路径/相对路径/网络路径/锚点(#name/#id)" 必须的属性
        target 窗口打开方式 _self(当前窗口)(default)/_blank(新建窗口)/_parent(父窗口)
        name 可作为锚点（其他标签的id属性也可做为锚点）
-->
<body>
    <a href="https://www.baidu.com/" target="_blank">在新窗口中打开百度</a>
    <a name="huilai1"></a>
    <a href="#huilai1">回到huilai1</a>
    <p id="huilai2"></p>
    <a href="#huilai2">回到huilai2</a>
</body>
```

## 7.图片、视频标签

```html
<!--
    图片标签<img> 行内元素；标签会在网页中创建一个占位空间并链接图片
        src 图片的URL 必须的属性
        alt 图片的代替文本，在图像无法显示时显示的文字
        title 鼠标悬停时显示的文字
        width/height 设置图片大小，单个设置时默认等比放缩。 百分比或px
        border 边框 px
        align 文本围绕方式
    视频标签<video></video> 
        src 视频的URL 必须的属性
        title 鼠标悬停时显示的文字
        width/height 设置视频大小，单个设置时默认等比放缩。 百分比或px
        controls 是否显示控制条
-->
<body>
    <a href="https://www.baidu.com/">
        <img src="https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png" alt="无法显示" title="百度一下" width="200px" border="2">
    </a>
    <video src="url" controls>
        不支持video标签时显示。
    </video>
</body>
```

## 8.表格标签

```html
<!--
    <table></table> 定义表格 块级元素
        align 对齐方式 left/center/right
        border 表格边框的宽度 px
        width/height 表格的宽度/高度 百分比或px
    <tr></tr> 定义表格的行 块级元素
        align 水平对齐方式
        valign 垂直对齐方式 top/bottom/middle
        bgcolor b
    <td></td> 定义表格的标准单元格 行内元素
        rowspan 纵向合并
        colspan 横向合并
    <th></th> 定义表头单元格（内容自动加粗居中）

    css样式 border-collapse: collapse; 合并表格边框
-->
<body>
    <table border="1" width="500px" align="center" style="border-collapse: collapse;">
        <tr>
            <th>班级</th>
            <th>姓名</th>
            <th>年龄</th>
        </tr>
        <tr align="center">
            <td rowspan="2">101</td>
            <td>张三</td>
            <td>7</td>
        </tr>
        <tr>
            <td colspan="2">李四6岁</td>
        </tr>
    </table>
</body>
```

## 9.表单与input标签

```html
<!--
    所有标签都有的属性：
        id 标识元素唯一性
        name 提交数据的参数名
        style 设置元素的行内样式（具体）
        class 设置元素的样式名
    <form></form> 定义表单 块级元素
            ***表单提交时必须设置表单元素的name属性值，用于获取数据
        action 提交表单的地址
        method 提交方式 get/post(服务器支持)
            get请求时将参数跟在地址栏后，不安全，传递数据有限，但是速度快，有缓存
            post将请求数据存放在请求体中
        target 打开窗口的方式 _self/_blank
        enctype 上传文件的表单需要设置值"multipart/form-data"，提交方式为post
    <input>标签 行内元素
        type 元素类型 
            text(文本框)/password(密码框)
            radio(单选框)/checkbox(复选框) 通过name属性分类；checked标记选中
            file(文件域)/hidden(隐藏域) 结合表单enctype属性
            button(普通按钮)/submit(提交按钮)/reset(重置按钮)
            date(日期框)
        value 元素值
        maxlength 元素最大长度
        readonly 只读
        disabled 禁用
-->
<body>
    <form action="https://www.baidu.com" method="get">
        文本框：<input type="text" value="shijin" readonly><br>
        密码框：<input type="password" maxlength="10"><br>
        单选框：<input type="radio" value="men" name="sex">男
        <input type="radio" value="women" name="sex">女<br>
        复选框：<input type="checkbox" value="1" checked name="box">1
        <input type="checkbox" value="2" name="box">2
        <input type="checkbox" value="3" name="box">3 <br>
        文件域：<input type="file" disabled><br>
        隐藏域：<input type="hidden" value="admin"><br>
        普通按钮：<input type="button"><br>
        提交按钮：<input type="submit"><br>
        重置按钮：<input type="reset"><br>
        日期框：<input type="date">
    </form>
</body>
```

## 10.表单中其他标签（textarea/lable/button/select）

```html
<!--
    <textarea></textarea> 多行文本输入
        cols/rows 宽度/行数
    <lable></lable> 文本标签
        for 点击时聚焦到for属性指向的id属性对应的标签
    <button></button> 按钮标签
        type 按钮类型 button(普通)/submit(提交)(default)/reset(重置)
        与input按钮的区别：除文本外可以添加其他标签，图片等
    <select></select> 下拉框标签
        multiple 多选
        size 同时显示选项个数
        <option></option> 下拉框的选项标签
            selected 选择元素
            disabled 禁用元素
            value 提交的文本（若没有该属性则提交双标签中的元素）
-->
<body>
    简介：<textarea name="intro" id="textarea" cols="30" rows="10"></textarea>
    <label for="textarea">聚焦到简介</label><br>
    <button type="button">按钮</button><br>
    <select name="city" id="city">
        <option disabled>北京</option>
        <option>上海</option>
        <option selected>广州</option>
        <option>深圳</option>
        <option>杭州</option>
    </select><br>
    <select name="city" id="city" multiple size="3">
        <option value="beijing">北京</option>
        <option>上海</option>
        <option selected>广州</option>
        <option>深圳</option>
        <option selected>杭州</option>
    </select>
</body>
```

## 11.常用标签实体与标签的分类

```html
<!--
    字符实体
        < &lt;
        > &gt;
        空格 &nbsp;
        版权 &copy;
    标签的分类
        块级元素 自动换行；可以设置元素的宽高等；默认宽度为页面的100%
        行内元素 不可以设置元素的宽高等
        行内块级元素 在行内但可以设置元素的宽高等
-->
<body>
    &lt;&nbsp;&nbsp;&copy;&nbsp;&gt;
</body>
```
