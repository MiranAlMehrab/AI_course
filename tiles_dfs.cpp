#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <stack>

using namespace std;

struct Action
{
    bool go_left;
    bool go_right;
    bool go_up;
    bool go_down;
};

struct Coordinate
{
    int x;
    int y;
};


int **matrix;
int **goal_matrix;
int number_of_elements = 3;
stack <string> action_queue;




void initializeMatrix()
{
  ifstream iFile;
  ifstream oFile;

  iFile.open("input.txt");
  oFile.open("output.txt");
  if(!iFile.is_open() || !oFile.is_open())
  {
    cout << "Error in opening file!" << '\n';
    exit(-1);
  }
  else
  {
    matrix = new int *[number_of_elements];
    goal_matrix = new int *[number_of_elements];

    for(int i=0;i<number_of_elements;i++)
    {
        matrix[i] = new int [number_of_elements];
        goal_matrix[i] = new int [number_of_elements];
    }

    for(int i=0;i<number_of_elements;i++)
    {
        for(int j=0;j<number_of_elements;j++)
        {
            iFile >> matrix[i][j];
            oFile >> goal_matrix[i][j];
        }
    }

    iFile.close();
    oFile.close();
    cout << "Initialization done!" << '\n';
  }
}


Action * initialize_action()
{
    Action *action = new Action[1];

    action->go_left = false;
    action->go_right = false;
    action->go_up = false;
    action->go_down = false;
    return action;
}


Action * find_branch(int i, int j)
{
    Action *action = initialize_action();

    if((j-1) >= 0) action->go_left = true;
    if((j+1) <= (number_of_elements-1)) action->go_right = true;
    if((i+1) <= (number_of_elements-1)) action->go_down = true;
    if((i-1) >= 0) action->go_up = true;

    return action;
}

void print_puzzle(int **arr)
{
    for(int i=0;i<number_of_elements;i++)
    {
        for(int j=0;j<number_of_elements;j++)
        {
            cout << arr[i][j] <<" ";
        }
        cout <<"\n";
    }
}


Coordinate * find_blank(int ** arr)
{
    Coordinate * coordinate = new Coordinate [1];
    for(int i=0;i<number_of_elements;i++)
    {
        for(int j=0;j<number_of_elements;j++)
        {
            if(arr[i][j] == 0)
            {
                coordinate->x = i;
                coordinate->y = j;
            }
        }
    }
    return coordinate;
}


int ** make_copy(int **arr)
{
    int ** temp;
    temp = new int *[number_of_elements];
    for(int i=0;i<number_of_elements;i++)
    {
        temp[i] = new int [number_of_elements];
    }

    for(int i=0;i<number_of_elements;i++)
    {
        for(int j=0;j<number_of_elements;j++)
        {
            temp[i][j] = arr[i][j];
        }
    }
    return temp;
}


bool check_goal(int **matrix, int **goal_matrix)
{

  for(int i=0;i<number_of_elements;i++)
  {
      for(int j=0;j<number_of_elements;j++)
      {
          if(matrix[i][j] != goal_matrix[i][j]) return false;
      }
  }
  return true;
}



void action_center(int **arr)
{
    if(check_goal(arr,goal_matrix))
    {
        cout <<"Goal found"<<endl;
        print_puzzle(arr);
        return;
    }
    print_puzzle(arr);


    Coordinate *coordinate = find_blank(arr);
    Action *action = find_branch(coordinate->x, coordinate->y);

    cout <<"x: "<< coordinate->x <<" y:  "<<coordinate->y<<endl;
    cout <<"left: "<< action->go_left <<" right: "<< action->go_right <<" up: "<< action->go_up <<" down: "<<action->go_down<<endl;

    if(action_queue.top()!="right") cout<<"Not right!"<<endl;
    cout <<"Hello"<<endl;
    if(action->go_left == true && action_queue.top()!="right")
    {
        cout <<"going left!"<<endl;
        int **temp = make_copy(arr);
        swap(temp[coordinate->x][coordinate->y],temp[coordinate->x][coordinate->y-1]);

        if(check_goal(temp,matrix))
        {
            cout <<"------------------------ Beware --------- initial matrix is back ------------------------"<<endl;
        }
        else if(check_goal(temp,goal_matrix))
        {
            cout <<"Goal found"<<endl;
            print_puzzle(temp);
            return;
        }
        else
        {
            action_queue.push("left");
            action_center(temp);
        }

    }
    if(action->go_right == true && action_queue.top()!="left")
    {
        cout <<"going right!"<<endl;
        int **temp = make_copy(arr);
        swap(temp[coordinate->x][coordinate->y],temp[coordinate->x][coordinate->y+1]);
        if(check_goal(temp,matrix))
        {
            cout <<"------------------------ Beware --------- initial matrix is back ------------------------"<<endl;
        }
        else if(check_goal(temp,goal_matrix))
        {
          cout <<"Goal found"<<endl;
          print_puzzle(temp);
          return;
        }
        else
        {
            action_queue.push("right");
            action_center(temp);
        }
    }
    if(action->go_down == true && action_queue.top()!="up")
    {
          cout <<"going down!"<<endl;
          int **temp = make_copy(arr);
          swap(temp[coordinate->x][coordinate->y],temp[coordinate->x+1][coordinate->y]);
          if(check_goal(temp,matrix))
          {
              cout <<"------------------------ Beware --------- initial matrix is back ------------------------"<<endl;
          }
          else if(check_goal(temp,goal_matrix))
          {
              cout <<"Goal found"<<endl;
              print_puzzle(temp);
              return;
          }
          else
          {
              action_queue.push("down");
              action_center(temp);
          }

      }
      if(action->go_up == true && action_queue.top()!="down")
      {
            cout <<"going up!"<<endl;
            int **temp = make_copy(arr);
            swap(temp[coordinate->x][coordinate->y],temp[coordinate->x-1][coordinate->y]);
            if(check_goal(temp,matrix))
            {
                cout <<"------------------------ Beware --------- initial matrix is back ------------------------"<<endl;
            }
            else if(check_goal(temp,goal_matrix))
            {
              cout <<"Goal found"<<endl;
              print_puzzle(temp);
              return;
            }
            else
            {
              action_queue.push("up");
              action_center(temp);
            }

      }

      if(!action_queue.empty())action_queue.pop();
}



int main()
{
    initializeMatrix();
    action_queue.push("nothing");
    //print_puzzle(matrix);
    //print_puzzle(goal_matrix);
    action_center(matrix);
    return 0;
}
