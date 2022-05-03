On Linux

%{
#define NUM 1
%}

%%
[0-9]+\.[0-9]+|[0-9]+ {return NUM;}
int|char|bool|void {return 2;}
[a-zA-Z]+[a-zA-Z0-9]* {return 3;}
%%


#include<stdio.h>
int main(int args, char*argv[]){
	int val;									//sudo apt install gcc
	
	while (val=yylex()){		
	switch(val){
	case 1:										//commands
	printf("\n%s-Number",yytext);				// lex lex.l(lex.l is file)(sudo apt-get install -y flex)
	break;										//gcc lex.yy.c -o a.out (if error gcc not recognized then install gcc)
	case 2:										//./a.out
	printf("\n%s-Keyword", yytext);			
	break;
	case 3:										//input 
	printf("\n%s-Identifier",yytext);			//4.5|abc|int
	break;
	}
}

return 0;
}

int yywrap(){return(1);}