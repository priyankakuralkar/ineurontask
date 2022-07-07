import logging
logging.basicConfig(filename= "task2.log",level=logging.DEBUG ,format = "%(asctime)s %(levelname)s %(message)s")
class my_list:
    def __init__(self,l):
        self.l =l

    def extract_list(self):
        try:
            logging.info("extract list from outer list")
            aaa =[]
            for i in self.l:
                if type(i)== list:
                    aaa.append(i)
            logging.info(f"extracted list is {aaa}")
        except Exceptiom as e:
            logging.error(e)

    def extract_dict(self):
        try:
            logging.info("extract dict from list")
            bbb =[]
            for i in self.l:
                if type(i)== dict:
                    bbb.append(i)
            logging.info(f"extracted dict is {bbb}")
        except Exception as e:
            logging.error(e)


    def extract_tuple(self):
        try:
            logging.info("extract tuple from list")
            ccc =[]
            for i in self.l:
                if type(i)== tuple:
                   ccc.append(i)
            logging.info(f"extracted tuple from list is {ccc}")
        except Exception as e:
            logging.error(e)


    def extract_number(self):
        try:
            logging.info("extract all numerical data from list")
            ddd = []
            for i in self.l:
                if type(i)== list or type(i)== tuple or type(i)==set :
                    for j in i:
                        if type(j)== int:
                          ddd.append(j)
                if type(i)== dict:
                    for k ,v  in i.items():
                        if type(k)== int:
                            ddd.append(k)
                        if type(v) == int:
                            ddd.append(v)
            return ddd
            logging.info(f"extract number from list is {ddd}")
        except Exception as e:
            logging.error(e)


    def sum_of_no_in_list(self):
        try:
            logging.info("sum of all integer in list")
            s1 = 0
            for i in self.l:
                if type(i)==list or type(i)==tuple or type(i)==set:
                    for j in i:
                        if type(j)== int:
                            s1 =s1 + j
                elif type(i)== int:
                    s1 = s1 + i
                if type(i)==dict:
                    for k,v in i.items():
                        if type(k)== int:
                            s1 =s1 + k
                        if type(v)== int:
                            s1 = s1 + v
            return s1
            logging.info(f"sum of all numbers is {s1}")
        except Exception as e:
            logging.error(e)


    def extract_oddno(self):
        try:
            logging.info("extract odd numbers in list")
            eee = []
            for i in self.l:
                if type(i)==list or type(i)==tuple or type(i)==set:
                    for j in i:
                        if type(j)== int and j % 2 !=0:
                            eee.append(j)
                if type(i)== dict:
                    for k,v in i.items():
                        if type(k)== int and k % 2 != 0 :
                          eee.append(k)
                        if type(v)== int and v % 2 != 0:
                            eee.append(v)
            logging.info(f"extracted odd number is  {eee}")
        except Exception as e:
            logging.error(e)


    def unwrap_fun(self):
        try:
            logging.info("unwrap th entire list ")
            fff = []
            for i in self.l:
                if type(i)== list or type(i)==tuple or type(i)== set:
                    for j in i:
                        if type(j)==int or type(j)== str:
                            fff.append(j)
                if type(i)== dict:
                    for k,v in i.items():
                        if type(k)==int or type(k)== str:
                            fff.append(k)
                        if type(v)== int or type(v)== str:
                            fff.append(v)
            return fff
            logging.info(f"unwrap entire list is {fff}")
        except Exception as e:
            logging.error(e)

    def occurance_in_list(self):
        try:
            logging.info("number of occurances in entire list ")
            l1 = self.unwrap_fun()
            ggg = {}
            for i in list(l1):
                  a= l1.count(i)
                  ggg[i]= a
            logging.info(f"occurence in list is {ggg}")

        except Exception as e:
            logging.error(e)

    def extract_keys(self):
        try:
            logging.info("extract keys in dict ")
            hhh =[]
            for i in self.l:
                if type(i)== dict:
                    for k,v in i.items():
                       hhh.append(k)
            logging.info(f"keys from dict are {hhh}")
        except Exception as e:
            logging.error(e)

    def extract_string(self):
        try:
            logging.info("extract string data from list")
            uuu = []
            for i in self.l:
                if type(i)== list or type(i)==tuple or type(i)==set:
                    for j in i:
                        if type(j)== str:
                            uuu.append(j)
                if type(i)== dict:
                    for k,v in i.items():
                        if type(k)== str:
                            uuu.append(k)
                        if type(v)==str:
                            uuu.append(v)
            return uuu
            logging.info(f"string element from list is {uuu}")
        except Exception as e:
            logging.error(e)


    def alnum_fun(self):
        try:
            logging.info("extract alnum in list")
            l2 = self.unwrap_fun()
            ppp = []
            for i in l2:
                if type(i)== str:
                    if i.isalnum():
                        ppp.append(i)
            return ppp
            logging.info(f"alnum values are {ppp}")
        except Exception as e:
            logging.error(e)

    def mul_fun(self):
        try:
           logging.info("multiplication of all int present in list")
           www = []
           m = 1
           for i in self.l:
               if type(i)==list or type(i)== tuple or type(i)==set:
                   for j in i:
                       if type(j)== int:
                         m = m * j

               if type(i)== dict:
                   for k in i.items():
                       for n in k:
                         if type(n)==int :
                           m = m* n
           return m

        except Exception as e:
            logging.error(e)











objlist = my_list([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
logging.info(objlist.extract_list())
logging.info(objlist.extract_dict())
logging.info(objlist.extract_tuple())
logging.info(objlist.extract_number())
logging.info(objlist.sum_of_no_in_list())
logging.info(objlist.extract_oddno())
logging.info(objlist.unwrap_fun())
logging.info(objlist.occurance_in_list())
logging.info(objlist.extract_keys())
logging.info(objlist.extract_string())
logging.info(objlist.alnum_fun())
logging.info(objlist.mul_fun())