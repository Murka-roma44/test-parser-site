def insert_newlines(string):
   col=len(string)
   col2 = col//80
   every=0
   str_list = list(string)
   if col2>0:
      for i in range(0,col2):
         every+=80
         while str_list[every]!=' ':
            every-=1
         else:
            str_list[every]='\n'
   string = ''.join(str_list)
   return(string)