from rest_framework import serializers
from .models import Author, Book, BorrowRecord, Member


class AuthorSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id' ,'first_name', 'last_name', 'bio']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerailizer(write_only = True ,required = False)              #Used for creating a new author 
    author_id = serializers.IntegerField(write_only = True, required = False)  #used for updtaing the author or for creating    the book of an author that already exist
    author_name = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Book
        fields = ['title', 'genre', 'publication_year', 'status', 'author', 'author_id', 'author_name']

    def create(self, validatetd_data):
        author_data = validatetd_data.pop("author", None)
        author_id = validatetd_data.pop("author_id", None)
        if author_data is not None:
            author, created = Author.objects.get_or_create(**author_data)
        elif author_id is not None:
            try:
                author = Author.objects.get(id = author_id)
            except Author.DoesNotExist:
                raise serializers.ValidationError(
                    {
                        "error" : "Author not found"
                    }
                )
        return Book.objects.create(author = author, **validatetd_data)
    
    def update(self, instance, validated_data):
        author_id = validated_data.pop("author_id", None)
        if author_id is not None:
            try:
                author = Author.objects.get(id = author_id)
                instance.author = author
            except Author.DoesNotExist:
                raise serializers.ValidationError("Author doesn't exist")
        instance.title = validated_data.get('title', instance.title)
        instance.publication_year = validated_data.get('publication_year', instance.publication_year)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.save()
        return instance

    def get_author_name(self, obj):
        return f'{obj.author.first_name} {obj.author.last_name}'




class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"


class AuthorBooksSerializer(serializers.ModelSerializer):
    books = BookSerializer(many = True)
    class Meta:
        model = Author
        fields = ['books']



class BookRecordSerializer(serializers.ModelSerializer):
    book_title = serializers.SerializerMethodField(read_only = True)
    member_name = serializers.SerializerMethodField(read_only = True)
    member = serializers.PrimaryKeyRelatedField(queryset = Member.objects.all(), write_only = True)
    book = serializers.PrimaryKeyRelatedField(queryset = Book.objects.all(), write_only = True)
    class Meta:
        model = BorrowRecord
        fields = ["book_title", "member_name", "member", "book", "borrow_date", "return_date"]

    def get_book_title(self, obj):
        return obj.book.title

    def get_member_name(self, obj):
        return obj.member.first_name        
    

class BorrowedByMemberSerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField()
    class Meta:
        model = BorrowRecord
        fields = ['book']

    def get_book(self, obj):
        return obj.book.title
    

class MemberWhoBorrowedABookSerializer(serializers.ModelSerializer):
    member = serializers.SerializerMethodField()
    class Meta:
        model = BorrowRecord
        fields = ['member']

    def get_member(self, obj):
        return obj.member.first_name