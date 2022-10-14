//Name : M.Nabeel, CMS ID: 023-21-0276, BS(CS)-III Section-B
//Instructor: Saif Hassan, Subject : DSA, Task: Next Word Prediction.

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

class Node{
    String data;
    Node next;

    Node(String data){
        this.data=data;
        this.next=null;
    }
}

class Task1{
    int count=0;
    public String readFile(String path){
        File myfile=new File(path);
        String line="";
        try {
            Scanner sc = new Scanner(myfile);
            while(sc.hasNext()){
                line+=sc.next()+" ";
                count++;
            }
            sc.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return line;
    }

    public String[] preprocess(String data){
        String cleaned_Data = "";
        // System.out.println(data.length());
        String[] word=new String[count];
        int j=0;
        for(int i=0;i<data.length();i++){
	        if(((data.charAt(i)>='a' && data.charAt(i)<='z') || (data.charAt(i)>='A' && data.charAt(i)<='Z'))){
	        	cleaned_Data+=data.charAt(i);
			}
            else if(data.charAt(i)==' '){
                word[j++]=cleaned_Data;
                cleaned_Data ="";
            }
    	}
        return word;
    }

    public Node createLLFromText(String[] arr){
        Node head=null;
	    Node currNode=null;
	    for(int i=0;i<count;i++){
            if(head==null){
                Node node=new Node(arr[i]);
                head=currNode=node;
            }
            else{
                Node node=new Node(arr[i]);
                currNode.next=node;
                currNode=node;
            }
	    }   
	    return head;
    }

    public String predictNextWord(String word,Node head){
        String token="";
        String arr[]=new String[2];
        for(int i=0;i<word.length();i++){
            if(word.charAt(i)!=' '){
                token+=word.charAt(i);
            }
            else{
                arr[0]=token;
                token="";
            }
        }
        arr[1]=token;
        String text="";
        Node ptr=head,nextPtr=head.next;
        while(nextPtr.next.next != null){
            if(ptr.data.equals(arr[0]) && nextPtr.data.equals(arr[1])){
                text+=nextPtr.next.data+" "+nextPtr.next.next.data+", ";
            }
            ptr=nextPtr;
            nextPtr=nextPtr.next;
        }
        return text;
    }

    public static void main(String[] args) {
        String filename="data.txt";
        Task1 obj=new Task1();
        String unclean_text=obj.readFile(filename);
        System.out.println(unclean_text);
        
        String[] word_array=obj.preprocess(unclean_text);
        Node head=obj.createLLFromText(word_array);
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter text for predict next text: ");
        String word=sc.nextLine();
        String predict_text=obj.predictNextWord(word, head);
        System.out.println(predict_text);
        sc.close();

    }
        
}
