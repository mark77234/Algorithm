class Solution {
    public int[] solution(int[] array) {
        int val = 0;
        int idx = 0;
        
        for (int i = 0; i < array.length; i ++){
            if (array[i] > val){
                val = array[i];
                idx = i;
            }
        }
        return new int[]{val,idx};
    }
}