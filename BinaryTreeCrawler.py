
class Node():
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
        self.parent=None



def insert_node():
    global root
    global cur_node
    new_node = Node(None)
    if(root.val == None):
        print "Give a value?"
        value = input()
        new_node.val = value
        root  = new_node
        cur_node = root
    else:
        print "Left or right?"
        ch = input()
        if(ch =='L'):
            if(cur_node.left==None):
                print "Give a value?"
                value = input()
                new_node.val = value
                cur_node.left = new_node
                new_node.parent = cur_node
                
            else:
                print "Cannot Add, Place not empty"

        elif(ch =='R'):
                if(cur_node.right==None):
                        print "Give a value?"
                        value = input()
                        new_node.val = value
                        cur_node.right = new_node
                        new_node.parent = cur_node
                                 
                else:
                        print "Cannot Add, Place not empty"

def move_node(st):
    global cur_node
    global root
    lst = list(st)
    lst_size = len(lst)
    aux_node = Node(None)
    aux_node = cur_node
    for x in range(lst_size):
        ch = lst[x]
        if (ch == 'L'):
            if(aux_node.left != None):
                aux_node = aux_node.left
            else:
                print "movement not possible !!!"
                return

        elif (ch == 'R'):
            if(aux_node.right != None):
                aux_node = aux_node.right
            else:
                print "movement not possible !!!"
                return

        elif(ch == 'P'):
            if(aux_node.parent != None):
                aux_node = aux_node.parent
            else:
                print "movement not possible !!!"
                return

        elif(ch =='r'):
            if(root.val != None):
                aux_node = root
            else:
                print "movement not possible !!!"
                return

        else:
            print "movement not possible !!!"
            return
    cur_node = aux_node


def print_tree(nd):
    h = height(nd)
    for i in range(1, h+1):
        
        print_level(nd, i)
        print "\n"
 
 

def print_level(nd , level):
    if nd is None:
        return
    if level == 1:
        print "%d" %(nd.val),
        
    elif level > 1 :
        print_level(nd.left , level-1)
        
        print_level(nd.right , level-1)
        
 

def height(node):
    if node is None:
        return 0
    else :
        
        lheight = height(node.left)
        rheight = height(node.right)
 
        
        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1


root = Node(None)
cur_node = root
sel = 0;
while(sel != 4):
    print "\n1. Move\n2. Add\n3. Print\n4. Exit\n"
    sel = input()
    if (sel==1):
        print "input movement pattern?"
        move_str = input()
        move_node(move_str)

    elif(sel ==2):
            insert_node()


    elif(sel == 3):
        if(root.val):
            
            print_tree(root)
        else:
            print "empty data"

    elif(sel ==4):
        exit()

    else:
        print "wrong choice !!!"
