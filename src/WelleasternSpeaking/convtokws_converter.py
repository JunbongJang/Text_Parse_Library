# encoding: utf-8
# for converting drill.txt files into drill_kws.txt
book_number = 1
unit_number = 1
step_number = 1

while(True):
	print ("book number:" + str(book_number))
	print ("unit number:" + str(unit_number))
	print ("step number:" + str(step_number))
	#file_name = input("Enter file's prefix name: ")
	folder_name = str(book_number)+"_"+str(unit_number)
	file_name = folder_name +"_drill_"+str(step_number)
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
				for ch in ['A:','B:','C:']:
					if ch in line:
						line=line.replace(ch,"")
						line=line.strip()
				for ch in ['.',',','?','!',';',':','"','”','“','\t']:
					if ch in line:
						line=line.replace(ch,"")
				new_file.write(line.lower())
		
		step_number +=1
		new_file.close()
		a_file.close()	
		
	except IOError:
		print ("This file does not exist!!!")
		print ("book number:" + str(book_number))
		print ("unit number:" + str(unit_number))
		print ("step number:" + str(step_number))
		unit_number +=1
		step_number = 1;
		if(unit_number == 5):
			book_number += 1
			unit_number = 1
		if(book_number == 5):
			break;