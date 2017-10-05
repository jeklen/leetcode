#include <iostream>
using namespace std;
struct node
{
	int x;
	node* next;
};

node* create(int n)
{
	node* head = new node;
	node* p = head;
	
	for (int i=0;i<n;i++)
	{
		node *temp = new node;	// new一个node指针
		temp->x = rand() % 100;
		p->next = temp;
		p = temp;
	}
	p->next = NULL;
	return head;
}

void display(node* head)
{
	node* p;
	p = head->next;		//p重新指向头结点的那个结点，即for循环创建的第一个结点
	if(p==NULL)
		cout << "NULL List";
	while(p!=NULL)
	{
		cout << p->x << " ";
		p = p->next;
	}
	cout << endl;
}

int main()
{
	node *list;
	list=create(10);
	
	return 0;
}

