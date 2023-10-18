from abc import ABC, abstractmethod

listaPessoas = []

# Classe PontoFunc
class PontoFunc:
    def __init__(self, mes, ano, nroFaltas, nroAtrasos):
        self.__mes = mes
        self.__ano = ano
        self.__nroFaltas = nroFaltas
        self.__nroAtrasos = nroAtrasos

    def getMes(self):
        return self.__mes

    def getAno(self):
        return self.__ano

    def getNroFaltas(self):
        return self.__nroFaltas

    def getNroAtrasos(self):
        return self.__nroAtrasos

    def lancaFaltas(self, nroFaltas):
        if nroFaltas >= 0:
            self.__nroFaltas += nroFaltas

    def lancaAtrasos(self, nroAtrasos):
        if nroAtrasos >= 0:
            self.__nroAtrasos += nroAtrasos

# Superclasse Funcionario
class Funcionario(ABC):
    def __init__(self, codigo, nome, pontoMensalFunc):
        self.__codigo = codigo
        self.__nome = nome
        self.__pontoMensalFunc = []

    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

    def getPontoMensalFunc(self):
        return self.__pontoMensalFunc

    def adicionaPonto(self, mes, ano, nroFaltas, nroAtrasos):
        novoPonto = PontoFunc(mes, ano, nroFaltas, nroAtrasos)
        self.__pontoMensalFunc.append(novoPonto)

    @abstractmethod
    def calculaSalario(self, mes, ano):
        pass

    @abstractmethod
    def calculaBonus(self, mes, ano, salario):
        pass

    @abstractmethod
    def imprimeFolha(self, mes, ano):
        pass

# Classe Professor
class Professor(Funcionario):
    def __init__(self, codigo, nome, titulacao, salarioHora, nroAulas):
        super().__init__(codigo, nome, [])
        self.__titulacao = titulacao
        self.__salarioHora = salarioHora
        self.__nroAulas = nroAulas

    def adicionaPonto(self, mes, ano, nroFaltas, nroAtrasos):
        super().adicionaPonto(mes, ano, nroFaltas, nroAtrasos)

    def getTitulacao(self):
        return self.__titulacao

    def getSalarioHora(self):
        return self.__salarioHora

    def getNroAulas(self):
        return self.__nroAulas

    def calculaSalario(self, mes, ano):
        totalFaltas = 0
        for ponto in self.getPontoMensalFunc():
            if ponto.getMes() == mes and ponto.getAno() == ano:
                totalFaltas += ponto.getNroFaltas()
        salarioProf = (self.__salarioHora * self.__nroAulas) - (self.__salarioHora * totalFaltas)
        return salarioProf

    def calculaBonus(self, mes, ano, salario):
        totalAtrasos = 0
        for ponto in self.getPontoMensalFunc():
            if ponto.getMes() == mes and ponto.getAno() == ano:
                totalAtrasos += ponto.getNroAtrasos()
        if totalAtrasos == 0:
            bonus = salario * 0.1
        else:
            bonus = (0.1-(totalAtrasos/100)) * salario
        return bonus

    def imprimeFolha(self, mes, ano):
        salario = self.calculaSalario(mes, ano)
        bonus = self.calculaBonus(mes, ano, salario)
        print(f"Codigo: {self.getCodigo()}")
        print(f"Nome: {self.getNome()}")
        print(f"Salario Líquido: {salario:.2f}")
        print(f"Bonus: {bonus:.2f}")
        
    def lancaFaltas(self, mes, ano, nroFaltas):
        if nroFaltas >= 0:
            for ponto in self.getPontoMensalFunc():
                if ponto.getMes() == mes and ponto.getAno() == ano:
                    ponto.lancaFaltas(nroFaltas)


    def lancaAtrasos(self, mes, ano, nroAtrasos):
        if nroAtrasos >= 0:
            for ponto in self.getPontoMensalFunc():
                if ponto.getMes() == mes and ponto.getAno() == ano:
                    ponto.lancaAtrasos(nroAtrasos)
                    
# Classe TecAdmin
class TecAdmin(Funcionario):
    def __init__(self, codigo, nome, funcao, salarioMensal):
        super().__init__(codigo, nome, [])
        self.__funcao = funcao
        self.__salarioMensal = salarioMensal

    def adicionaPonto(self, mes, ano, nroFaltas, nroAtrasos):
        super().adicionaPonto(mes, ano, nroFaltas, nroAtrasos)

    def getFuncao(self):
        return self.__funcao

    def getSalarioMensal(self):
        return self.__salarioMensal

    def calculaSalario(self, mes, ano):
        totalFaltas = 0
        for ponto in self.getPontoMensalFunc():
            if ponto.getMes() == mes and ponto.getAno() == ano:
                totalFaltas += ponto.getNroFaltas()
        salarioTec = self.__salarioMensal - ((self.__salarioMensal / 30) * totalFaltas)
        return salarioTec

    def calculaBonus(self, mes, ano, salario):
        totalAtrasos = 0
        for ponto in self.getPontoMensalFunc():
            if ponto.getMes() == mes and ponto.getAno() == ano:
                totalAtrasos += ponto.getNroAtrasos()
        if totalAtrasos == 0:
            bonus = salario * 0.08
        else:
            bonus = (0.08-(totalAtrasos/100)) * salario
        return bonus

    def lancaFaltas(self, mes, ano, nroFaltas):
        if nroFaltas >= 0:
            for ponto in self.getPontoMensalFunc():
                if ponto.getMes() == mes and ponto.getAno() == ano:
                    ponto.lancaFaltas(nroFaltas)

    def lancaAtrasos(self, mes, ano, nroAtrasos):
        if nroAtrasos >= 0:
            for ponto in self.getPontoMensalFunc():
                if ponto.getMes() == mes and ponto.getAno() == ano:
                    ponto.lancaAtrasos(nroAtrasos)
                    
    def imprimeFolha(self, mes, ano):
        salario = self.calculaSalario(mes, ano)
        bonus = self.calculaBonus(mes, ano, salario)
        print(f"Codigo: {self.getCodigo()}")
        print(f"Nome: {self.getNome()}")
        print(f"Salario Liquido: {salario:.2f}")
        print(f"Bonus: {bonus:.2f}")

if __name__ == "__main__":
    funcionarios = []
    prof = Professor(1, "Joao", "Doutor", 45.35, 32)
    prof.adicionaPonto(4, 2021, 0, 0)
    prof.lancaFaltas(4, 2021, 2)
    prof.lancaAtrasos(4, 2021, 3)
    funcionarios.append(prof)
    tec = TecAdmin(2, "Pedro", "Analista Contabil", 3600)
    tec.adicionaPonto(4, 2021, 0, 0)
    tec.lancaFaltas(4, 2021, 3)
    tec.lancaAtrasos(4, 2021, 4)
    funcionarios.append(tec)
    for func in funcionarios:
        func.imprimeFolha(4, 2021)
        print()
