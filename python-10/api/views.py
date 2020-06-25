from collections import Counter

from rest_framework import status
#ref:  https://www.django-rest-framework.org/api-guide/views/#api_view
from rest_framework.decorators import api_view

from rest_framework.response import Response

#ref: https://docs.python.org/3/library/collections.html


@api_view(['POST'])
def lambda_function(request):
    question = request.data.get('question')
    solution = []
    c = Counter(question)
    # n least common elements
    for n, count in c.most_common():
        for _ in range(count):
            solution.append(n)
    return Response({'solution': solution}, status=status.HTTP_200_OK)