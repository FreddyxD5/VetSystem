from django.core.paginator import Paginator, InvalidPage
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 5

class Pagination:
     """ Paginacion

        Clase encargada de gestionar la paginación de un conjunto de elementos y retornar información correspondiente
        a dicho conjunto de datos.

        ATRIBUTOS

        page                    : página por defecto
        page_size               : número de elementos por página por defecto
        paginator_class         : clase paginadora


        PARÁMETROS

        queryset                : consulta
        serializador            : serializador para retornar los datos en formato JSON
        request                 : petición enviada a la vista, sirve para obtener valores como page_size y page


        RESPUESTA

        elementos_por_pagina    : número de elementos que contendrá cada página
        total_elementos         : total de elementos paginados
        numero_paginas          : total de páginas
        pagina                  : página actual
        data                    : datos paginados
        """  

        page = DEFAULT_PAGE
        page_size = DEFAULT_PAGE_SIZE
        pagination_class = Paginator


        def paginar_consulta(self, queryset, serializador , request):
            #Validamos si se ha enviado algun parametro, ya sea page_size o page,
            # en caso contrariose toma el por defecto
            self.page_size = int(request.query_params.get('page_size', self.page_size))
            self.page = int(request.query_params.get('page',self.page))

            paginador = self.paginator_class(queryset, self.page_size)

            try:
                pagina = paginador.page(self.page)
            except:
                return Response({'error':'No existe esta pagina'})

            serializador = serializador(pagina, many=True)

            return Response({
                'elementos_por_pagina': self.page_size,
                'total_elementos': pagina.paginator.count,
                'numero_paginas': pagina.num_pages,
                'pagina': pagina.number,
                'data':serializador.data
            })