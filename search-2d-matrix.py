#TC: O(mlogN) 
#SC: O(1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)  
        
        for i in range(m):  #iterating through the matrix
            low = 0  #setting low pointer in i'th index
            high = len(matrix[0])-1  # #setting high pointer to last index in i'th row
            
            while low<=high: #loop will run until the low crosses high
                mid = low+(high-low)//2  #to avoid interger over flow we are calculating the mid
                
                if target == matrix[i][mid]: return True  #if the target is eual to the matrix val we are retiurning true
                
                if target < matrix[i][mid]:  #if the target is less than the matrix val we are moving our high pointer to mid-1
                    high = mid-1
                else:
                    low = mid +1 #if the target is greater than the matrix val we are moving our low pointer to mid+1
                               
        return False  #if the target is not found we are returning false