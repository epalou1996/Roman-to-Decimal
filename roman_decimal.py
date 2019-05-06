

class Desromanizacion():
	#This class execute 3 basic actions, check syntaxix, chevy roman number validity and transform it to a decimal form.

	def __init__(self,numero):
		self.numero=numero

	def Verificacion(self):
		#Uppercase the number, checks string only alphabet caracters, and that those letters match the ones in the roman numeric alphabet
		if self.numero.isalpha()==True:
			self.numero=self.numero.upper()
			print(self.numero)

			#Big f***** if
			if (self.numero.find("A")==-1 and self.numero.find("B")==-1 and self.numero.find("E")==-1 and 
			self.numero.find("F")==-1 and self.numero.find("G")==-1 and self.numero.find("H")==-1 and self.numero.find("J")==-1 and 
			self.numero.find("K")==-1 and self.numero.find("N")==-1 and self.numero.find("O")==-1 and self.numero.find("P")==-1 and 
			self.numero.find("Q")==-1 and self.numero.find("R")==-1 and self.numero.find("S")==-1 and self.numero.find("T")==-1 and 
			self.numero.find("U")==-1 and self.numero.find("W")==-1 and self.numero.find("Y")==-1 and self.numero.find("Z")==-1 and 
			self.numero.find("IIII")==-1 and self.numero.find("XXXX")==-1 and self.numero.find("CCCC")==-1 and self.numero.find("DDDD")==-1 and 
			self.numero.find("VVVV")==-1 and self.numero.find("LLLL")==-1) :		

				print("Roman numeral: ",self.numero," has a valid alphabetical format")
				y=True
				return y
			else:
				print("Roman numeral: ",self.numero," is not valid, please try again")	
				y=False
				return y
		else:
			print("Roman numeral: ",self.numero," is not valid, please try again")
			y=False
			return y

	def Desromanizar (self):

		#This transform each letter in a number, and compares to its predecesor, so if something like IX gets in, it will add 1, when the I is in the while
		#and then when the X is readed, it will ad 8 points so that the number is 9
		listado2=[]			
		comprobante2=True
		for i in self.numero:
			
			if i=="I":
				listado2.append(1)
			elif i=="V":
				listado2.append(5)
			elif i=="X":
				listado2.append(10)
			elif i=="L":
				listado2.append(50)
			elif i=="C":
				listado2.append(100)
			elif i=="D":
				listado2.append(500)
			elif i=="M":
				listado2.append(1000)		
		cantidad=len(listado2)
		p=0
		while p<cantidad:
			if 5*listado2[p-1]==listado2[p] and p!=0:
				listado2[p]=listado2[p-1]*3	
			elif 10*listado2[p-1]==listado2[p] and p!=0:
				listado2[p]=listado2[p-1]*8			
			elif int(listado2[p-1])>int(listado2[p]) and p!=0:
				pass				
			elif p==0:	
				pass			
			else:			
				comprobante2=False	
			p=p+1
		p=0
		decimal=0
		if comprobante2==True:
			while p<cantidad:
				decimal=decimal+listado2[p]
				p=p+1
			print("Roman numeral: ",self.numero, " is equivalent to: ",str(decimal))
			y=True
			return y
		else:
			print("Roman numeral: {} has an invalid form, check if the number has the correct syntaxis")
			print("Remember that numerals like IL are not valid, the apropiate form is XLIX")
			y=False
			return y


#Simple Run with check and posibility of retry until you get your number
comprobante=False
while comprobante==False:
	numero_recibido=input("Insert the roman numeral you´d like to transform: ")
	num=Desromanizacion(numero_recibido)
	comprobante=num.Verificacion()
	if comprobante==False:
		pass
	else:
		comprobante=num.Desromanizar()