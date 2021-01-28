#include "ds.h"
#include <string.h>

# ifdef sun
# define const
# endif

extern const char *
okfail(int val)
{
    return val ? "[ OK ]" : "[FAIL]";
}

//testting
void test_parray(int, char *);
void test_stack(int,char *);
void test_queue(int,char *);

int main(int argc, char *argv[])
{
	printf("Hello C-Free!\n");
	
	int n = 5;
	char A[5] = {2,4,6,8,10};
	char B[5] = {'a','b','c','d','e'};	
     
    test_parray(n,A);
    test_stack(n,B);
    test_queue(n,A);
    
	return 0;
}

void test_parray(int n,char *A)
{
    PARRAY 	pa;
    char *	s;
    int		i;
	
	printf("====PARRAY START===========\n");
    pa = paMake(3,1);

    for (i = 0; i < n; i++)
	paAdd(pa,(void*)A[i]);
	
	int * a = paLast(pa);
	paPrev(pa);
	int k = paCurrent(pa);
	k = pa->curr;
	printf("s = %d\n",a);
	
    for (s = (char*)paFirst(pa);s; s = (char*)paNext(pa))
	printf("s = %d\n",s);
    printf("===============\n");

    printf("paLast() returns %d\n",(char*)paLast(pa));
    printf("paNext() returns %d\n",(char*)paNext(pa));
    printf("Current is now %d\n",(char*)paCurrent(pa));

    printf("Clearing current.\n");
    paClearCurrent(pa);
    printf("Current is now %d\n",(char*)paCurrent(pa));
    printf("paPrev() returns %d\n",(char*)paPrev(pa));
    printf("paNext() returns %d\n",(char*)paNext(pa));
    printf("paLast() returns %d\n",(char*)paLast(pa));
    printf("paPrev() returns %d\n",(char*)paPrev(pa));
    printf("Current is now %d\n",(char*)paCurrent(pa));
    printf("paFirst() returns %d\n",(char*)paFirst(pa));
    printf("Current is now %d\n",(char*)paCurrent(pa));
    printf("Setting current to %d\n",3);
    paSetCurrent(pa,3);
    printf("Current is now %d\n",(char*)paCurrent(pa));

    printf("paPrev() returns %d\n",(char*)paPrev(pa));
    printf("paPrev() returns %d\n",(char*)paPrev(pa));
    printf("paCurrent() returns %d\n",(char*)paCurrent(pa));
    printf("paNext() returns %d\n",(char*)paNext(pa));
    printf("Removing 3rd element\n");
    paRemove(pa,3);
    for (s = (char*)paFirst(pa);s; s = (char*)paNext(pa))
	printf("s = %d\n",s);
    printf("===============\n");

    printf("Removing 1st element\n");
    paRemove(pa,1);
    printf("Removing -3 element\n");
    paRemove(pa,-3);

    for (s = (char*)paFirst(pa);s; s = (char*)paNext(pa))
	printf("s = %d\n",s);
    printf("====PARRAY END=============\n");     
} 

void test_stack(int n,char *A)
{
    STACK st;
    char *s;
    int pushed = n;
	
	printf("====STACK START===========\n");
    st = stkMake();

    while (n--)
	stkPush(st,A[n]);

    printf("Pushed %d elements onto the stack\n",pushed);
    printf("stkSize() reports = %d\n",stkSize(st));
    while ((s = (char*)stkPop(st)))
	printf("s = %c, stack size = %d\n",s,stkSize(st));
	printf("====STACK END=============\n");   
} 

void test_queue(int n,char *A)
{
    QUEUE 	q;
    char *	s;
    int		i;
	
	printf("====QUEUE START===========\n");
    if (n == 1)
    {
	printf("Use: %d arguments\n",A[0]);
	printf("    The arguments are placed in the queue and various test\n"
	       "    routines are performed on the queue.\n");	
    }
    q = qMake();

    for (i = 0; i < n; i++)
    {
	qAdd(q,(void*)A[i]);
	printf("current should be last: %s\n",
	       okfail(qLast(q) == qCurrent(q)));
    }

    for (s = (char*)qFirst(q);s; s = (char*)qNext(q))
	printf("s = %d\n",s);
    printf("===============\n");

    printf("qLast() returns %d\n",(char*)qLast(q));
    printf("qNext() returns %d (should be (null))\n",(char*)qNext(q));
    printf("Current is now %d\n",(char*)qCurrent(q));
    printf("qPrev() returns %d (should be same as last)\n",
	   (char*)qPrev(q));
    printf("Current is now %d\n",(char*)qCurrent(q));
    printf("qNext() returns %d\n",(char*)qNext(q));
    printf("qFirst() returns %d\n",(char*)qFirst(q));
    printf("qPrev() returns %d\n",(char*)qPrev(q));
    printf("Current is now %d\n",(char*)qCurrent(q));
    printf("qNext() returns %d\n",(char*)qFirst(q));

    printf("\n\nUSE AS LINKED LIST:\n");
    printf("Current is now %d\n",(char*)qCurrent(q));
    printf("qPrev() returns %d\n",(char*)qPrev(q));
    printf("qPrev() returns %d\n",(char*)qPrev(q));
    printf("qCurrent() returns %d\n",(char*)qCurrent(q));
    printf("qPrev() returns %d\n",(char*)qPrev(q));
    printf("etc....\n");
    printf("====QUEUE END=============\n");
} 