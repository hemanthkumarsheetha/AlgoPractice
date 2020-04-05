L=[]
  for string in b:
    st={}
    for i in string:
      if string.count(i) == len(string):
        st[i]=string.count(i)
        break
      if i not in st.keys():
        st[i] = string.count(i)
    L+=[st]