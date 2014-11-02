/*算法导论 10.4-5 O(n)时间非递归遍历二叉树
一、题目
写一个O(n)时间的非递归过程，输出给定的含n个结点的二叉树中每个结点的关键字。要求只能用除树本身以外的固定量的额外存储空间，而且在过程中不能修改该树，哪怕是暂时的

二、思考
采用类似中序遍历的处理方法，对一个结点，可以分为以下几种情况

1.从父结点进入子结点进行处理

（1）如果有左孩子，就处理左孩子

（2）返回到自己

（3）访问自己

（4）如果有右孩子，就处理右孩子

（5）返回到自己的父结点

2.从左孩子返回，说明左孩子已经处理过，自己还没访问，自己的右孩子也没有处理过，就进行1-（2）

3.从右孩子返回，说明左右孩子都已经处理，自己也访问过，就返回到更上层

4.返回到根结点时，遍历结束

三、代码
*/
#include <iostream>

using namespace std;

/********10.4-5****************************************************************/
//二叉树结点
struct node
{
	int key;//值
	node *left;//指向左孩子
	node *right;//指向右孩子
	node *parent;//指向父结点
	node(){}//构造函数
	node(int x):key(x),left(NULL),right(NULL){}
};
//二叉树
struct tree
{
	node *root;
	tree():root(NULL){}
};
//遍历并输出
void Tree_Print(tree *T)
{
	node *t = T->root;
	//t指向当前处理的结点
	while(t){
		//(1)如果当前结点有左孩子，则先处理其左孩子
		if ( t-> left ){
			t = t->left;
			continue;
		}
		//如果当前结点没有左孩子，就访问自己并处理其左孩子
		else{
			//(3)访问自己
			cout << t->key <<' ';
			//(4)如果当前结点有右孩子，则处理其右孩子
			if ( t-> right) {
				t = t->right;
				continue;
			}
			//(5)如果结点既没有左孩子，又没有右孩子
			//向上找，找到下一个待处理的点，过程类似于中序遍历
			//下一个待处理的点的特点是：有右孩子且右孩子还未处理过，下一个待处理的就是这个右孩子
			while(1) {
				//如果当前孩子是其父结点的左孩子，说明其父结点及父结点的右孩子还没有处理过
				//t->parent满足条件1.未访问过2.有右孩子3.其右孩子没处理过，于是处理其右孩子
				if (t == t->parent->left && t->parent->right){
					//父结点还没有访问过，先访问父结点，再处理父结点的右孩子
					cout << t->parent->key <<' ';
					t = t->parent->right;
					break;
				}
				// t ->parent满足条件1.未访问过2.无右孩子
				if (t == t->parent->left && t->parent->right == NULL)
					//访问父结点，并继续向上寻找
					cout<< t->parent->key<<' ';
				//t->parent满足条件1.访问过2.如果有右孩子，一定已经处理过了，所以不考虑
				//继续向上寻找
				t = t-> parent;
				//一直找到根结点也没有找到符合要求的结点，那么二叉树已经遍历完成
				if(t == T->root){
					cout<<endl;
					return;
				}
			}
		}
	}
}
/*input:0=NIL
12 7 3
15 8 0
4 10 0
10 5 9
2 0 0
18 1 4
7 0 0
14 6 2
21 0 0
5 0 0
*/
int main()
{
	//构造一棵树按照10.4-1
	int i;
	node A[11];//这个数组仅仅用于构造10.4-1中的树，在遍历时不使用
	for (i = 1; i <= 10; i++)
	{
		int key, left, right;
		cin>>key>>left>>right;
		A[i].key = key;
		if(left)
		{
			A[i].left = &A[left];
			A[left].parent = &A[i];
		}
		else A[i].left = NULL;
		if(right)
		{
			A[i].right = &A[right];
			A[right].parent = &A[i];
		}
		else A[i].right = NULL;
	}
	//生成一棵树
	tree *T = new tree();
	T->root = &A[6];
	//10.4-5
	Tree_Print(T);
	return 0;
}
 

