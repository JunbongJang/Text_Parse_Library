# encoding: utf-8
book_number = 1
unit_number = 1

while(True):
	print ("book number:" + str(book_number))
	print ("unit number:" + str(unit_number))
	#file_name = input("Enter file's prefix name: ")
	folder_name = str(book_number)+"_"+str(unit_number)
	file_name = folder_name +"_expr"#"_vocab"
	try:
		a_file = open(folder_name+"\\"+file_name+".txt", "r", encoding ="utf-8") 
		new_file = open(folder_name+"\\"+file_name+"_kws.txt", "w", encoding ="utf-8")
		
		for line in a_file: 
			print (line)
			if(line != "\n"):
				for ch in ['’']:
					if ch in line:
						line=line.replace(ch,"'")
				for ch in ['-']:
					if ch in line:
						line=line.replace(ch," ")
				for ch in ['A:','B:']:
					if ch in line:
						line=line.replace(ch,"")
						line=line.strip()
				for ch in ['.',',','?','!',';',':','"','”','“','\t']:
					if ch in line:
						line=line.replace(ch,"")
				new_file.write(line.lower())
		
		unit_number +=1
		new_file.close()
		a_file.close()	
		
	except IOError:
		print ("This file does not exist!!!")
		print ("book number:" + str(book_number))
		print ("unit number:" + str(unit_number))
		book_number +=1
		unit_number =1
		
		if(book_number == 5):
			break;