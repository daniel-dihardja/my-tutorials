import { Form, redirect } from "@remix-run/react";
import type { ActionFunctionArgs } from "@remix-run/node";
import { Button } from "~/components/ui/button";
import { Input } from "~/components/ui/input";

// Action function to handle login
export async function action({ request }: ActionFunctionArgs) {
  // TODO: Add login logic here

  // Redirect to /app after successful login
  return redirect("/app");
}

export default function Login() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-gray-50 px-4 py-12 dark:bg-gray-900">
      <div className="w-full max-w-sm rounded-2xl border border-gray-200 bg-white p-6 shadow-md dark:border-gray-700 dark:bg-gray-800">
        <div className="mb-6 text-center">
          <h1 className="text-2xl font-bold sm:text-3xl text-gray-800 dark:text-gray-100">
            MyTutorials
          </h1>
        </div>

        <Form method="post" className="space-y-4">
          <div>
            <Input
              name="email"
              type="email"
              placeholder="Username / Email address"
              inputMode="email"
              autoComplete="email"
              className="text-base"
            />
          </div>

          <div>
            <Input
              name="password"
              type="password"
              placeholder="Password"
              autoComplete="current-password"
              className="text-base"
            />
          </div>

          <Button type="submit" className="w-full py-3 text-base">
            Login
          </Button>
        </Form>
      </div>
    </div>
  );
}
