import { ArrowLeftIcon } from "@radix-ui/react-icons";
import Link from "next/link";
import { notFound } from "next/navigation";

interface PageProps {
	params: { id: string };
}

interface Post {
	userId: number;
	id: number;
	title: string;
	body: string;
}

interface User {
	id: number;
	name: string;
}

export default async function PostDetails({ params }: PageProps) {
	const postId = params.id;

	// Busca os dados da postagem
	const resPost = await fetch(
		`https://jsonplaceholder.typicode.com/posts/${postId}`,
	);
	if (!resPost.ok) {
		// Se a postagem não for encontrada, retorna um 404
		notFound();
	}
	const post: Post = await resPost.json();

	// Busca os dados do autor
	const resUser = await fetch(
		`https://jsonplaceholder.typicode.com/users/${post.userId}`,
	);
	const user: User = await resUser.json();

	return (
		<div className="container mx-auto px-4 py-8">
			<Link href="/" className="mb-4 hover:underline">
				<ArrowLeftIcon className="h-7 w-7" />
			</Link>
			<div className="container flex flex-col justify-center items-center mt-5">
				<h1 className="scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight first:mt-0">
					{post.title}
				</h1>
				<h4 className="scroll-m-20 text-xl font-semibold tracking-tight mt-3">
					Por {user.name}
				</h4>
				<p className="leading-7 [&:not(:first-child)]:mt-6">{post.body}</p>
			</div>
		</div>
	);
}
