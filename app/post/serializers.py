from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True, max_length=255)
#     author = serializers.CharField(read_only=True)
#     content = serializers.CharField(required=True, read_only=True)
#     created_date = serializers.DateTimeField()
#
# # abstract method를 다 받아야한다고 함.
# # model.serialize는 그냥 필드인데#
# # 디폴트는 그냥생기고
# # create들어있고, 업데이트 들어있고,


    class Meta:

        # 예시로 이렇게 커스텀하게 쓸수있음
        # title = serializers.CharField(read_only=False)
        # read_only가 뭐냐면. 그러니까 설명하니가 애매한데
        # 직렬화를 하면 데이터를 뿌려주는데 반대로 거기서 우리한테 보내주면
        # 저장도 할 수 있잖아요. 그런데 저장은 안되게 막고 보내는 것만.
        # 받아와서 저장을 하는것도 하거든요.
        #
        # 아마 dafault가 True? False?
        # False로 두려면 뭘 추가적으로 줘야되거든요.

        model = Post
        fields = (
            'id',
            'title',
            # 'author',
            'content',
            'created_date',
        )