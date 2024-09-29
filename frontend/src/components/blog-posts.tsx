"use client";

import { useState } from "react";
import { CustomizedPagination } from "./customized-pagination";
import { Post } from "./post";
import { Input } from "./ui/input";

interface BlogPostsProps {
	allPosts: Post[];
	posts: Post[];
	currentPage: number;
	totalPages: number;
}

export function BlogPosts({ allPosts, posts, currentPage, totalPages }: BlogPostsProps) {
	const [searchTerm, setSearchTerm] = useState("");

	// Se o searchTerm estiver vazio, mostre todas as postagens
	// Caso contrário, filtre as postagens com base no título
	const displayedPosts = searchTerm
		? allPosts.filter((post) =>
				post.title.toLowerCase().includes(searchTerm.toLowerCase()),
			)
		: posts;

	return (
		<div className="container mx-auto px-4 py-8">
			<div className="flex items-center gap-2 justify-between">
				<h1 className="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl">
					Clarice Posts
				</h1>
				<Input
					type="text"
					placeholder="Pesquisar postagens..."
					value={searchTerm}
					onChange={(e) => setSearchTerm(e.target.value)}
					className="rounded px-4 py-2 w-1/2"
				/>
			</div>

			<div className="space-y-4 mt-7">
				{displayedPosts.length > 0 ? (
					displayedPosts.map((post) => <Post key={post.id} {...post} />)
				) : (
					<p>Nenhuma postagem encontrada</p>
				)}
			</div>

			{/* Exibe paginação apenas se não houver pesquisa ativa */}
			{searchTerm === "" && (
				<div className="mt-8 flex justify-center">
					<CustomizedPagination
						currentPage={currentPage}
						totalPages={totalPages}
					/>
				</div>
			)}
		</div>
	);
}
