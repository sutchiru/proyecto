import math

def promedio(lista):
    """
    Calcula el promedio de una lista de números, ignorando valores no finitos,
    con mayor precisión en la suma para minimizar errores de punto flotante.
    
    Parámetros:
    -----------
    lista: list
        Lista de variables aleatorias.
    
    Retorna:
    --------
    promedio: float
        El promedio de los valores finitos en la lista.
    """
    vals = []
    for v in lista:
        if math.isfinite(v):
            vals.append(v)

    
    suma = 0.0
    for val in vals:
        suma += val

    
    return suma / len(vals) if vals else float('nan')


def mediana(vals_in):
    
    """
    calcula la mediana de una lista conteniendo una
    variable categoria nominal
    Parametros
    -----------
    vals: list
    lista de categotias
    Retorna
    -------
    mediana: str
    la mediana de la muestra
    """
    #se eliminan valores que sean NaNs
    vals=[]
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
#ordenar la lista
    vals.sort()

    if len(vals)% 2!=0:
        k= len(vals)//2
        mediana= vals[k]            
    else: 
        k= len(vals)//2 
        mediana= (vals[k-1]+ vals[k])/2
    return mediana

def moda(vals):
    
    """
    calcula la moda de una lista conteniendo una
    variable categoriva nominal
    Parametros
    -----------
    vals: list
    lista de categotias
    Retorna
    -------
    moda: str
    la moda de la muestra
    """
    #encontrar el conjunto de elementos unicos
    categorias=[]
    for v in vals:
        if v not in categorias:
            categorias.append(v)
    #obtener el numero de cuentas en la muestra
    cuenta=[]
    #para cada una de las categorias
    
    
    for c in categorias:
        n=0
        for val in vals:
            if val==c:
                n=n+1
        cuenta.append(n)

    #guess and check
    i_max=0
    val_max=cuenta[0]
    for i in range(1,len(cuenta)):
        if cuenta[i]> val_max:
            i_max=i
            val_max=cuenta[i]
    #determinar todas las categorias que tengan el numero
    #maximo de cuentas
    
    modas= []
    for i in range(len(cuenta)):
        if cuenta[i]== val_max:
            modas.append(categorias[i])
    
    #retorno la moda
    #moda= categorias[i_max]
    return modas

def rango(vals_in):
    
    """
    calcula el rango de una lista conteniendos
    Parametros
    -----------
    vals: list
        lista de numeros
    Retorna
    -------
    rango: float
        rango de los valores (excluye nans)
    """
    
    vals=[]
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
    return max(vals)-min(vals)

def varianza(vals_in):
    
    """
    calcula varianza de una lista de numeros
    Parametros
    -----------
    vals: list
        lista de numeros
    Retorna
    -------
    varianza: float
        varianza de los valores (excluye NaNs)
    """
    
    vals=[]
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
    desviaciones=[]
    prom= promedio(vals)
    for i in vals:
        calculo= (i-prom)**(2)
        desviaciones.append(calculo)
    suma= sum(desviaciones)
    varianza= (1/len(vals)*suma)
        
    return varianza
        
def desviacion_estandar(vals_in):
    """
    calcula desviacion estandar de una lista de numeros
    Parametros
    -----------
    vals: list
        lista de numeros
    Retorna
    -------
    desviacion estandar: float
        desviacion de los valores (excluye NaNs)
    """
    
    vals = []
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
    prom = promedio(vals)
    # estimamos las desviaciones cuadraticas medias
    dcm = []
    for i in vals:
        dcm.append((i - prom) ** 2)
    varianza = sum(dcm) / len(vals)  # Dividir por n (población completa)
    return varianza ** (1 / 2)
    
def percentil(vals_in, q, interpolacion="lineal"):
    """
    Calcula el percentil de una lista de números. Ignora valores NaN.
    
    Parámetros:
    -----------
    vals_in: list
        Lista con los números.
    q: float
        Percentil a calcular (entre 0 y 100).
    interpolacion: str
        Método de interpolación ("lineal" es el único implementado).
    
    Retorna:
    --------
    percentil: float
        Percentil de los números (excluyendo NaNs).
    """
    # Eliminar valores NaN
    vals=[]
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)

    vals.sort()  # Ordenar la lista

    if interpolacion == "lineal":
        
        ieff = (len(vals) - 1) * (q / 100)
        i = int(ieff) 
        j = min(i + 1, len(vals) - 1)  
        fraction = ieff - i  

        # Interpolación lineal
        percentile = vals[i] + (vals[j] - vals[i]) * fraction
        return percentile

def iqr(vals_in):
    
    """
    calcula el rango intercuartilico. ignora valores nan
    Parametros
    -----------
    vals: list
        
    Retorna
    -------
    IQR: float
        el rango intercuartilico (excluye NaNs)
    """
    vals=[]
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
            
    iqr= percentil(vals,75)-percentil(vals,25)
    return iqr

    
def mad(vals_in):
    
    """
    calcula el MAD de una lista de valores. ignora valores nan
    Parametros
    -----------
    vals_in: list
            lista de numeros
        
    Retorna
    -------
    IQR: float
        MAD de los valores (excluye NaNs)
    """
    vals=[]
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
            
    med= mediana(vals)
    desviaciones_med=[]
    for v in vals:
        desviaciones_med.append(abs(v-med))
    mad= mediana(desviaciones_med)
    return mad

def covarianza(x,y):
    """
    calcula la covarianza de una lista de valores, ignora valores NaN
    
    Parámetros
    -----------
    x,y: list
        lista de números
    Retorna
    -------
    covarianza: float
        covarianza de los valores
    """
    x_vals=[]
    y_vals=[]
    if len(x) == len(y):
        for i in range(len(x)):
            if math.isfinite(x[i]) and math.isfinite(y[i]):
                x_vals.append(x[i])
                y_vals.append(y[i])
    else:
        print("los largos no coinciden")
            
    xmean= promedio(x_vals)
    ymean= promedio(y_vals)
    # Calcular la covarianza
    sum_cov = sum((xi - xmean) * (yi - ymean) for xi, yi in zip(x_vals, y_vals))
    
    # Covarianza
    covarianza = sum_cov / (len(x_vals) - 1)  # Si es muestra, usar N-1
    
    return covarianza

def correlacion(x, y):
    """
    Calcula la correlación de Pearson entre dos listas de valores. Ignora valores NaN.
    Parámetros:
    -----------
    x, y: list
        Listas de valores numéricos. Deben tener la misma longitud.
    Retorna:
    --------
    correlacion: float
        Coeficiente de correlación de Pearson.
    """
    x_vals, y_vals = [], []
    for xi, yi in zip(x, y):
        if math.isfinite(xi) and math.isfinite(yi):
            x_vals.append(xi)
            y_vals.append(yi)
    
    cov = covarianza(x_vals, y_vals)
    std_x = desviacion_estandar(x_vals)
    std_y = desviacion_estandar(y_vals)
    
    return cov / (std_x * std_y)
             
