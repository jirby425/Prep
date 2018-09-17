public class problem1 {

	//need to know that there is at most 128 charcters

	
	public static  boolean isUnique (String str){
		for (int i=0; i < str.length(); i++)
			for(int j=0; j < str.length(); j++)
				if (str.charAt(i) == str.charAt(j) && i != j) 
					return false;
		return true;			
	}
	
	public static boolean isUnique2(String str){
		if (str.length() > 128)	
			return false;	
		int []char_count = new int[128];
		for(int i =0; i < str.length(); i++){
			int val = str.charAt(i);
			if (char_count[val] > 0){
				return false;	
			}
			else
				char_count[val]++;
		}	
		return true;	
	}	
		

	public static void main (String[] args){
	String[] words = {"hello", "my", "name", "is", "jackson"};
		for (String word : words){
			System.out.print(isUnique(word));	
			System.out.println(isUnique2(word));	
		}	
	}

}




