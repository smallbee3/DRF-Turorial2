from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.compat import authenticate
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAdminUser, AllowAny

from post.models import Post
from post.serializers import PostSerializer

from rest_framework import generics, mixins


# 믹스인 순서가 중요해요, 다른것 상관업슨ㄴ데 항상 제너릭ㄴ이 끝에 와야되요.
class PostList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):




    # 이게 뭐 좀.. 아까 시리얼라이져 불러와서 거기 모델을 넣고 막막 했었잖요
# 이즈 밸리드. 막 그런거 있잫ㄴ아요 공통조ㅓㄱ으로 하는거
# 포스트객체 불러오는거 시리얼라이저
# 그거 관련된거를 얘가 다해줘요
# 어떤 거 쓸건지만 하면되요
# 그러고 페이지 네이팅도 되구요. 예를 들어 10개씨ㅣㄱ 페이지로 보여주고 싶다.
# 그러면 10개씩 유알엘이 나눠지겠죠

# 예를들어 리스트하면 이렇게 쭉 난왔잖아요.
# ㅂ페이지 네이터 2개 만 주면 1,2 만 아오겠죠.

# ?page=2
# 왠만한 핑료하겠다하는ㅇ 기능은 다 있어요
# 필터도 잇고, 검색하는 것 있잖아요. 필터나 정렬 예가 다 같고있거든요.
# 원시적으로하면 일ㅇ리이 다 해야되는데

# 그걸 제너릭 에이파이이 븅가 가지고있어요.

# 피룻적으로 해야되는게 있는데 쿼리셋이랑 시리어라이져 언더바 클래스 이거 두개는 꼭 줘야되요.\
# 쿼리셋에는 얘를주면되요. 우리가 쓸려는 객체
    # 지금은 그냥 이렇개 외우세요 올로보내는거 리스트니까
    # 나중에 디테일도 포싀트 오브젝트 올로 보내요.
    # 그런데 거기서 알아서 피케이로 꺼내서 줘요.
    # 그리고 씨리얼라ㅣㅇ져 언더바 클래스는 포스트 씨리얼라이제잉져 주면 디요.

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        AllowAny,
    )
    # 그래서 퍼미션스 거기 보면은 세이프 메소드가 있거든요. 겟 해드 옵션 이거 세개중에 하나가 오면 그냥 상관 없는거. 이거 만약 메서드가 세개중에 하나있으면 무조건 트루를 리턴하고 아닐경우에는
    # 헤드 퍼미션이라는 거ㅔ 리케스트와 뷰를 받는데
    # 뷰는 이 퍼미션이 들어있는 뷰 있잫ㄴ아요. 그게 오는데 그거 점 get_object()하면 이게와요 쿼리셋. 포스트가 오겠죠. 지금 이거는  지금이ㅡㄴ 이게 없는데 그게 오거든요. 예를들어 디테일뷰
    # 겟 오브젝트를 하면

    # 아무튼 그게 ..
    # 이거
    #
    # 아무튼 퍼미션 클래스는 이렇게써요.
    # 그니까 그 유저객체 전달할대 리퀘스트.유저로 다 작성자라고 넣어주거든요
    # 그런데 유저쪽 시리얼라이져가 되어있어야 포스트에 유저객체를 넣어줄때 유저 시리얼라이져로 통과한거를 넘어간거를 넘어가야
    # 되는것 같아요. 그럼 리퀘스트 유저를 그니가
    # 어나니머스를 리퀘스트 유저로 바꿔줘ㅇ야.

    # 로그인뷰는 이런걸 받겠죠
    # {
    # "username": "nachwon",
    # "password": "aksdjlk"
    # }
    # 통과시켜서 로그인 시키면 되겠죠
    #

    #  wjgmlsms xhzmsdlwmddmfh goshktj dlfjsep xhrmsdlfkd dbwjrorcp wbrh. dbwj tlfldjffkdlwudp wlqdjsjgdmsrjrjemsdy. dlrp djqtdjtj
    #  이거때문인것 같아요.

    # apis.py
    # soundhub/users
    # authentification 헤더에 그 유저가 밖히는 거거든요.
    # 원래 없었는데 이거 하면 여기 밖히잖아요. 로그인하면 헤더에 밖혀요
    # 리퀘스트.유저는 현재로그인한 유저로 바뀌고.
    # 아마그랬던것 같아요.
    #
    # 04:53

    # CRUD만 제대로해도 에이피아이 느리게 나오냐 이런 소리는 안나올거에요.
    # 요기요 같은거. 음식점 리스트. 그거 이걸로 해야되죠.
    # 레스토랑 리스트. 시알유디 있어야되죠.
    # 씨알유디.
    # 이걸로 후딱 짜버리면 되겠죠.
    # 지금 믹스인즈 했잖아요.
    # 이것도 귀찮아서 줄인게 있어요.
    # 이걸 다지우고요
    # 결국 최종적으로 이것 밖에 안쓴거같아요
    # class PostList(generics.ListCreateAPIView):
    # 이러헥 짜져있어서.리스트랑 크리에이트를 합쳐놓은거 있잖아요.
    # 왜냐면 이걸 자주 쓰기 때문이겠죠.
    # 아까 디이에프 필요없어요.
    # 믹스이즈 갖고 있죠.
    # 밑에 겟 포스트까지 써주죠.
    # 이게 끝이에요.
    # 프로젝트 시작하면 이건 달고 시작하면 되죠.
    # 얘는 리스트였잖아요.
    # 얘도 바꿀 수 있겠죠
    # 얘도 웃긴게 포스트 디테일 이잫ㄴ아요.
    # 얘는 그럼 지금 겟 이랑 겟이니까 알유디가있죠.
    # 그럼 RetrieveUpdateDestroyAPIView가 있어요
    #




        # 오디오 믹스 / soundhub.utils-get  permissions.py
        # /projects/django/audiomix-project/soundhub/utils




    # 이거 두개를 주고, 아직까지 얘는 그게 없어요. 아까 클래스 베이스드 뷰 보면 겟풋
    # 이런걸 함수로 정의해줬잫나요 아직 그런게 없거든요 만약에 해줄려면 직접 짤수도 있"ㅇ요. 겟요청은 어쩌고 풋ㅇㅛ청은 어쩌고
    # 그게 클래스드베이스드 뷰 겠죠
    # 그러면 의미가 없으니까
    # 여기서도 제너릭 뷰와 함께 쓸 수있는게 믹스인이라는게 있는데
    # 이거는 얘도 같은데서 불ㅇ러와요;.

    # 믹스인스라고 제너릭이랑 같은



    # 리스트 가보면 우리가 해준게 있어요.
    # 리스트 믹스인 보는 중.
    #

    # 그리고 크리에이트 보면 퍼폼 ㅅ크리에이트는 세이브하는 것 저희가 한거 그대로죠.
    # 아까 이스밸리드면 세이브
    #
    # 레이저ㅡ 익셉션 트루

    # 레이즈 익셉션이 통과못하면 ㅁ머추는 것 같거든요.



    # 이걸 했었어야 했나. 기억이 안나는데..

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # ---
    #
    # 포스트 리스트는 겟요청은 아무나할수있어도되잖아요
    # 그런데 로그인된 유저만 할 수있어야
    # 된다:
    # 하면그런걸 하는게
    # 이런걸 너주면
    #  되거든요:
    #
    #   IsAuthenticated

    # ㅁ이안에 여러개가 퍼미션이 들어갈거잫ㄴ아요.
    # 이게 다 트루가 되야되요
    # 인증이 되었는지 보고 인증이 되었으면 트루를 리넡해주겠죠.
    # allowany이거는 모든.


    # ----


    # 아까 겟포스트를 함수로 만든다고 했잖아요. 겟요청이 ㄱ들어오면 실행되고 그런식으로
    # 그거는 아마 에이피아이뷰가 하겠죠.

    # 라이크는 그냥 원시적인 걸로 짜시면 될 것 같아요.


    # 그리고 유알엘에서 얘도 바꿔줘야되거든요.



# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = (IsAdminUser, )
#
#     def create(self, request, *args, **kwargs):
#         data = {
#
#
#         }
#         serializer = self.get_serializer(data=data)
#         serializer.is_valid()
#         self

#
# @csrf_exempt
# def post_list(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         # 객체가 하나가 아니잖아요. 매니트루를 하면 하나씩 씨리얼라이제이션 해주는 거에요
#         # 아마 이게 없으면 이상한.. 에러가 나네요..
#         return JsonResponse(serializer.data, safe=False)
#         # 형태로만 만들어주는 것 같음.
#         # 사실상 이걸 해준거죠
#         # return HttpResponse(JSONRenderer().render(serializer.data))
#         # json.dump쓰는데 왜 여기서 렌더러는 어디서 튀어나온거지?
#         # 만약에 겟요청이 왔는데 신기한걸 하고싶다 하면 원시적으로 짜는게 나을 수 있어요.
#         # 왜냐면 이거를 안쓰고 하는게,
#
#     # 글쓰는거 추가 해볼게요.
#     if request.method == 'POST':
#         print(request.POST)
#
#         data = JSONParser().parse(request)
#         data['author'] = 1
#         # 1단계
#         # return 값이 없어서 에러 뜨게 해놓고 서버창에서 출력되는 값 확인
#         # <QueryDict: {'title': ['Test Post2'], 'content': ['Hello world!!']}>
#         # return JsonResponse(data)
#
#         # 2단계
#         serializer = PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#         # 400으로 붙여줘야 인식함. 예전 보충강의시간에 경험해본것으로기억
#
#
# @csrf_exempt
# def post_detail(request, pk):
#     if request.method == 'GET':
#         post = Post.objects.get(pk=pk)
#         serializer = PostSerializer(post)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         print(data)
#         data['author'] = 1
#         post = Post.objects.get(pk=pk)
#         serializer = PostSerializer(post, data=data, partial=False)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == "PATCH":
#         data = JSONParser().parse(request)
#         print(data)
#         data['author'] = 1
#         post = Post.objects.get(pk=pk)
#         serializer = PostSerializer(post, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#
#     elif request.method == "DELETE":
#         post = Post.objects.get(pk=pk)
#         post.delete()
#         return HttpResponse(status=204)









# 스니펫은 우리 포스트 모델
# 리스트니까 다가져와야죠.
# 시리얼라이져넣어서 json리스판스로 돌려주는 거에요.


# localhost:8000  가보면 json 데이터 있는데
# 이걸 프론트에서 받아서 그냥 쓰는것

# - - - - - -
# ex)
# 예시 하나 보여드릴게요.
# 뭐가 잔뜩 오는데 이걸 갔다 쓰죠.
# 이게 오면
# json loads해서 request해서
# 딕셔너리가 되서 그냥 쓰면 되죠.

# 자바스크립트는 그냥 바로 딕셔너리 처럼 쓸 수잇어요.
# 예를들어 reponse['appnews']치면 그냥 튀어나와요
# - - - - - -



# 엄밀히 말하면,
# json 형태로된 텍스트를 보내는 거죠.



#           * * * * *


# 이제 레스트를 생각할 때가 됬어요.

# posts 리스트 이렇게 이름 붙이고.
# 포스트 모델들을 보여주는 거에요.
# 그러면 그 목록에서 할 수 있는일이.

# CRUD
# 프로그램이라고 부르려면 기본적으로 이거정도는 해야된다는 느낌


# 여기서 create 하면 생성
# retrive는 읽기. 이거 하면 뭐가 오죠. 포스트 리스트가 오죠
# update가 필요할까요? 디테일에 가서 업대이트

# 넣고싶으면 넣을 수 있어요.
# 어떤 리스트가 보는 유알엘이 업데이트 요청을 하면 어떤 특정한.
# 업데이트인데 다른 기능을 하면 RESTful(명시적이)하지 않잖아요.
# D까지는 늘려면 늘 수 있겠네요.
# 어쨋든 보통 CRD 까지는 넣을 수 있겠네요.


# 원래 우리는 add , 이런식으로.
# 지금 기능이 별로 없어서 그런데 나중에 crud를 쓰거든요.
# 저희가 지금까지 쓴 요청이 get/post밖에 없었는데

# c = post
# r = get
# u = put / patch
# d = delete

# url이 명사고 무슨짓을 할지는 http요청이 동사가 되는거에요
# 이게 100% Restful하게는 못하는 것같아요.

# ex)
# post/like
# 이렇게 파야됨.


# post/1/
# 좋아요를 하면 어떤 요청을 보내야되나.
# post요청이 있는데 뭐가 말이안되요.

# 그래서 투스콥스오브 장고 보면 그책에도 이 내용이 나오는데
# 장고가 그 자채가 restful 과 잘 안맞다고 한대ㅔ요.
# url 마음대로 짤 수 있는건 매한가지인데 왜 안맞다고 하는거지..

# 원래 restful 끝에 trailing slash

# 어떤 요청을 보냈는지 ...
# 프론트 사람들이 이걸보고
# if 따라함:

    # 유저애ㅔ 게[ㅅ요청을 보내면 목록은 이렇게 뜨고

# 깃허브는 문서화.
# 그래서 깃북은 꼭 안써도 되는것 같아요. 너무 느려요


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



    #그래서 에러가 뜨면 안되요.
# 만약에 못찾는다 그러면 이런게 와야되요.
# not found
# 그런데 웬만한거는 얘가 다해줘요