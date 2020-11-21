// necessary header files
#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>

// using the standared namespace
using namespace std;

// getInput() method with argument two arrays and two variables to count the valid and invalid scores
// since this function is not returning anything ,that's why validCount and invalidCount is reference variables
// call by reference method
void getInput(int validScores[],int invalidScores[],int &validCount,int &invalidCount){
    string filename;
    // getting filename from user
    cout<<"Enter the input file to read : ";
    cin>>filename;
    // filename = "input.txt";
    //creating ifstream variable
    ifstream fin;
    // opening file in reading mode
    fin.open(filename,ios::in);
    int score;
    // checking if file is opened
    if(fin){
        // then using while loop untill end of the file is reached
        while(!fin.eof()){
            fin>>score;  // reading score
           
            // if score is valid
            if(score>=0 && score<=100){
                // storing this score in validScores at validCount and then incrementing validCount
                validScores[validCount] = score;
                validCount++;
            }
            // if score is invalid
            else{
                // storing this score in invalidScores at invalidCount and then incrementing invalidCount
                invalidScores[invalidCount++] = score;
            }
        }
    }
    // if file is not opened the print the message and exit
    else{
        cout<<"File couldn't be opened !!"<<endl;
        exit(1);
    }
    fin.close();   // closing fin 
}
// printScores() method with argument and an int array , size and 
// a reference to ofstream object to write in file
void printScores(int arr[], int n, ofstream &fout){
    // iterating through the array
    for(int i=0;i<n;i++){
        // writing to the file using fout .... setw(5) is used to set the width
        fout<<setw(5)<<arr[i];
        // if 5 score are printed then print a new line
        if((i+1)%5==0){
            fout<<endl;
        }
    }
}

// lowestHighestAverage() method with argument and an int array , size and
// a reference to ofstream object to write in file
void lowestHighestAverage(int scores[],int n, ofstream &fout){
    int sum=0;    // to store sum
    int min = scores[0];   // setting min and max to first value of the array
    int max = scores[0];
    for(int i=0;i<n;i++){
        // calculating max
        if(scores[i]>max){
            max = scores[i];
        }
        // calculating min
        if(scores[i]<min){
            min = scores[i];
        }
        // adding all to sum
        sum+=scores[i];
    }
    // calculating average
    float average = (float)sum/n;
    // writing min,max and average to file using fout
    fout<<"\nThe highest good score is "<<max<<endl;
    fout<<"The lowest good score is "<<min<<endl;
    fout<<"The average of good score is "<<average<<endl;
}
// function to sort the score 
// this is simply selection sort apporach
void sortGoodScores(int arr[], int n){
    int min_index;
    int temp;
    for(int i=0;i<n-1;i++){
        min_index = i;
        for(int j=i+1;j<n;j++){
            if(arr[j]<arr[min_index]){
                min_index = j;
            }
        }
        
        temp = arr[i];
        arr[i] = arr[min_index];
        arr[min_index] = temp;
        
    }
}
// main method
int main()
{
    // creating two arrays
    int validScores[50];
    int invalidScores[50];
    // to store count of respsctive type of score
    int validCount=0;
    int invalidCount=0;

    ofstream fout;     //creating an ofstream object
    // opening the output.txt in out mode
    fout.open("output.txt",ios::out);
    // if file is not opened then printing the message and exit
    if(!fout){
        cout<<"output file can't be opened !!"<<endl;
        exit(1);
    }
    // calling getInput() to get the respsctive scores and counts
    getInput(validScores,invalidScores,validCount,invalidCount);
    
    
    // if file is not empty means there are some score ... 
    // checking with 1 as there may be some newlines intead of scores
    if((validCount+invalidCount)>1){
        //writing number of bad scores to file 
        fout<<invalidCount<<" bad scores: "<<endl;
        // writing bad scores to file by passing fout object
        printScores(invalidScores,invalidCount,fout);
        fout<<endl<<endl;  // writing endl
        
        //writing number of goog scores to file 
        fout<<validCount<<" good scores: "<<endl;

        // if validCount is > 0 then doing all the statistics on validScores
        if(validCount>0){
            // writing good scores to file by passing fout object
            printScores(validScores,validCount, fout);
            fout<<endl;   // writing endl
            // calling lowestHighestAverage to calulate min.max , average and write to file using fout
            lowestHighestAverage(validScores,validCount,fout);
            
            // calling sortGoodScores to sort the scoress
            sortGoodScores(validScores,validCount);
            
            //writing msg to file 
            fout<<"\nSorted good Scores :"<<endl;
            // writing sorted good scores to file by passing fout object
            printScores(validScores,validCount,fout);
        }
    }
    // if there is no valid scores then simply writing to file 
    else{
        fout<<"No score available";
    }
    fout.close(); // closing fout
}