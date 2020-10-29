#!/usr/bin/env python3
# The line above ^ is important. Don't leave it out. It should be at the
# top of the file.

import cgi, cgitb # Not used, but will be needed later.

def judge_type(x):
    if(x=="+"):
        return str(int(form['screena'].value)+int(form['screenb'].value))
    elif (x=="-"):
        return str(int(form['screena'].value)-int(form['screenb'].value))
    elif (x=='*'):
        return str(int(form['screena'].value)*int(form['screenb'].value))
    elif (x=="/"):
        return str(int(form['screena'].value)/int(form['screenb'].value))

print("Content-type: text/html\n\n")

form = cgi.FieldStorage()
if "screena" not in form or "screenb" not in form:
    print("<H1>Error</H1>")
    print("Please fill in the name and addr fields.")
# Output to stdout, CGIHttpServer will take this as response to the client

print('''<html>
<head>
	<title>jsss</title>
    <style type="text/css">
    	table{
    		
    		margin:0 auto;
            
    	}
		
    	
    	.but_ac{
    		width: 80px;
    		height: 60px;
    		background-color : lightgray;
    		font-size: 1.2em;
    	}
    	.but{
    		width: 80px;
    		height: 60px;
    		background-color : lightgray;
    		font-size: 1.2em;
    	}
    	.screen1{
    		width: 265px;
            height: 70px;
            font-size: 1.5em;
            color: white;
            background-color: black;
            text-align:right; 
    	}
		.screen2{
    		width: 265px;
            height: 70px;
            font-size: 1.5em;
            color: white;
            background-color: black;
            text-align:right; 
    	}
		.op{
			width: 80px;
            height: 70px;
            font-size: 1.5em;
            color: white;
            background-color: black;
            text-align:right; 
    	}
		
		
		td
		{
			text-align:center;
		}
		.buts{
			width: 160px;
    		height: 60px;
    		background-color : lightgray;
    		font-size: 1.2em;
		}
		.butx:active{
			background-color : gray;
		}

    </style>

    <script type="text/javascript">
    	window.onload=function(){
    	   var result;
           var str=[];
    	   var num=document.getElementsByClassName("but");
		   var scr1=document.getElementsByClassName("screen1")[0];
    	   var scr2=document.getElementsByClassName("screen2")[0];
           for(var i=0;i<num.length;i++)
           {

            	num[i].onclick=function(){

					if(this.id=="AC_1"){
						scr1.value="";
					}
					else if(this.id=="AC_2"){
						scr2.value="";
					}
					else if (this.id=="back_1"){      
					  scr1.value=scr1.value.substr(0,scr1.value.length-1);
					}
					else if (this.id=="back_2"){      
					  scr2.value=scr2.value.substr(0,scr2.value.length-1);
					}
					else if(scr1.value==""&&this.id=="._1"){
						 scr1.value="0.";
					 }
					 else if(scr1.value==""&&this.id=="._2"){
						 scr2.value="0.";
					 }
					 else if(this.id=="1_1"||this.id=="2_1"||this.id=="3_1"||this.id=="4_1"||this.id=="5_1"||this.id=="6_1"||this.id=="7_1"||this.id=="8_1"||this.id=="9_1"||this.id=="0_1"||this.id=="._1")
					 {
						scr1.value+=this.value;
					 }
					   else if(this.id=="1_2"||this.id=="2_2"||this.id=="3_2"||this.id=="4_2"||this.id=="5_2"||this.id=="6_2"||this.id=="7_2"||this.id=="8_2"||this.id=="9_2"||this.id=="0_2"||this.id=="._2")
					 {
						scr2.value+=this.value;
					 }
					 else if(this.id=="+_1")
					 {
						op.value+=this.value;
					 }
					 else if(this.id=="-_1")
					 {
						op.value+=this.value;
					 }
					 else if(this.id=="*_1")
					 {
						op.value+=this.value;
					 }
					 else if(this.id=="/_1")
					 {
						op.value+=this.value;
					 }
					 else{
						src1.value+="1";
					 }
				}
			}	

		}
    
    </script>

</head>
<body>
<form name="input" action="../cgi-bin/post.py" method="post">
<table width="100%" align="center">
<tr>
	 <td><table width="50%">
		  <tr>
			  <td colspan="3"><input class="screen1" type="text" name="screena"/></td>
		  </tr>
		  <tr>
			<td><input class="but_ac but" id="AC_1" type="button" value="AC" style="color: orange"></td>
			<td colspan="2"><input class="but_ac but" style="width: 180px" id="back_1"type="button" value="<-" style="color: orange"></td>
		  </tr>
		  <tr>
			<td><input class="but" id="7_1" type="button" value="7"></td>
			<td><input class="but" id="8_1"type="button" value="8"></td>
			<td><input class="but" id="9_1"type="button" value="9"></td>
		  </tr>
		  <tr>
			<td><input class="but" id="4_1" type="button" value="4"></td>
			<td><input class="but" id="5_1"type="button" value="5"></td>
			<td><input class="but" id="6_1"type="button" value="6"></td>
		  </tr>
		  <tr>
			<td><input class="but" id="1_1"type="button" value="1"></td>
			<td><input class="but" id="2_1"type="button" value="2"></td>
			<td><input class="but" id="3_1"type="button" value="3"></td>
		  </tr>
		  <tr>
			<td colspan="2"><input class="but" id="0_1"type="button" value="0" style="width: 180px"></td>
			<td><input class="but" id="._1"type="button" value="."></td>
		  </tr>
		 

	</table></td>
	<td><table>
	<tr>
		  <td><input maxlength="1" class="op" type="text" name="op" id= "op"/></td>
		  </tr>
		  <tr>
			<td><input class="butx but" id="/_1"type="button" value="/"></td>
		  </tr>
		  <tr>
			<td><input class="butx but" id="*_1"type="button" value="*"></td>
		  </tr>
		  <tr>
			<td><input class="butx but" id="-_1"type="button" value="-"></td>
		  </tr>
		  <tr>
			<td><input class="butx but" id="+_1"type="button" value="+"></td>
		  </tr>
		  
	</table>
	
	
	</td>

	<td><table width="50%" >
		   <tr>
			  <td colspan="3"><input class="screen2" type="text" name="screenb" value="''')
print(judge_type(form['op'].value))
print('''"/></td>
		  </tr>
		  <tr>
			<td><input class="but_ac but" id="AC_2" type="button" value="AC" style="color: orange"></td>
			<td colspan="2"><input class="but_ac but" style="width: 180px" id="back_2"type="button" value="<-" style="color: orange"></td>
		  </tr>
		  <tr>
			<td><input class="but" id="7_2"type="button" value="7"></td>
			<td><input class="but" id="8_2"type="button" value="8"></td>
			<td><input class="but" id="9_2"type="button" value="9"></td>
		  </tr>
		  <tr>
			<td><input class="but" id="4_2"type="button" value="4"></td>
			<td><input class="but" id="5_2"type="button" value="5"></td>
			<td><input class="but" id="6_2"type="button" value="6"></td>
		  </tr>
		  <tr>
			<td><input class="but" id="1_2"type="button" value="1"></td>
			<td><input class="but" id="2_2"type="button" value="2"></td>
			<td><input class="but" id="3_2"type="button" value="3"></td>
		  </tr>
		  <tr>
			<td colspan="2"><input class="but" id="0_2"type="button" value="0" style="width: 180px"></td>
			<td><input class="but" id="._2"type="button" value="."></td>
		  </tr>
		 

	</table></td>
</tr>
</table>
<div align="center">
<input class="buts" id="submit" type="submit" value="SUBMIT" width="100%">
</div>
</form>


</body>
</html>''')