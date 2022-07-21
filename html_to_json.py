def read_file(filename):
	'''
	repr : function takes html as input and genrate there appropriate JSON
	'''
	try:
		if not os.path.exists("json_output"):
			os.mkdir("json_output")
		json_store = list()		
		with open(filename, 'r',encoding="utf8") as f:
			text = f.read()
			store = html_to_json.convert(text)	
			json_store.append(store)
			save_file = "json_output/" + filename.split(".")[0].split('\\')[1] + ".json"
			with open(save_file,  "w") as file:
				json.dump(json_store, file,ensure_ascii=False,indent=4)			
		return save_file
	except Exception as e:
		return e

if __name__ == "__main__":
	import requests, json, os
	import html_to_json
	import sys,glob
	
	if sys.argv:
		if len(sys.argv) > 1:
			print("[INFO] Start execution..")
			htmldir = glob.glob(sys.argv[1]+"/*.html")
			for html in htmldir:
				save_file = read_file(html)
				print("[INFO] Json file store at : ",os.path.abspath(save_file))
		else:
			print("[INFO] Please enter the folder path.")