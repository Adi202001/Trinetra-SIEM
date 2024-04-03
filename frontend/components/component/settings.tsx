/**
 * This code was generated by v0 by Vercel.
 * @see https://v0.dev/t/wg094JdlA3M
 */
import Link from "next/link"
import { Button } from "@/components/ui/button"
import { CardTitle, CardDescription, CardHeader, CardContent, Card, CardFooter } from "@/components/ui/card"
import { TableCell, TableRow, TableHead, TableBody, Table } from "@/components/ui/table"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { Select } from "@/components/ui/select"
import { Checkbox } from "@/components/ui/checkbox"

export function Settings() {
  return (
    <div className="flex flex-col w-full min-h-screen">
      <header className="flex items-center h-16 px-4 border-b shrink-0 md:px-6">
        <Link className="flex items-center gap-2 text-lg font-semibold sm:text-base mr-4" href="#">
          <FrameIcon className="w-6 h-6" />
          <span className="sr-only">Acme Inc</span>
        </Link>
        <nav className="hidden font-medium sm:flex flex-row items-center gap-5 text-sm lg:gap-6">
          <Link className="text-gray-500 dark:text-gray-400" href="#">
            Projects
          </Link>
          <Link className="text-gray-500 dark:text-gray-400" href="#">
            Deployments
          </Link>
          <Link className="text-gray-500 dark:text-gray-400" href="#">
            Analytics
          </Link>
          <Link className="text-gray-500 dark:text-gray-400" href="#">
            Logs
          </Link>
          <Link className="font-bold" href="#">
            Settings
          </Link>
        </nav>
        <div className="flex items-center w-full gap-4 md:ml-auto md:gap-2 lg:gap-4">
          <Button className="rounded-full ml-auto" size="icon" variant="ghost">
            <img
              alt="Avatar"
              className="rounded-full border"
              height="32"
              src="/placeholder.svg"
              style={{
                aspectRatio: "32/32",
                objectFit: "cover",
              }}
              width="32"
            />
            <span className="sr-only">Toggle user menu</span>
          </Button>
        </div>
      </header>
      <main className="grid min-h-[calc(100vh_-_theme(spacing.16))] gap-4 p-4 md:gap-8 md:p-10">
        <div className="max-w-6xl w-full mx-auto grid gap-2">
          <h1 className="font-semibold text-3xl">Settings</h1>
        </div>
        <div className="grid md:grid-cols-[180px_1fr] lg:grid-cols-[250px_1fr] items-start gap-6 max-w-6xl w-full mx-auto">
          <nav className="text-sm text-gray-500 grid gap-4 dark:text-gray-400">
            <Link className="font-semibold text-gray-900 dark:text-gray-50" href="#">
              User Management
            </Link>
            <Link href="#">System Configuration</Link>
            <Link href="#">Alerts & Notifications</Link>
          </nav>
          <div className="grid gap-6">
            <Card>
              <CardHeader className="pb-0">
                <CardTitle>User Management</CardTitle>
                <CardDescription>Administer user accounts, roles, and permissions.</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="flex flex-col gap-4">
                  <Button className="rounded-lg" size="icon">
                    Add User
                  </Button>
                  <Table>
                    <TableHead>
                      <TableRow>
                        <TableCell className="w-1/3">User</TableCell>
                        <TableCell>Role</TableCell>
                        <TableCell>Permissions</TableCell>
                      </TableRow>
                    </TableHead>
                    <TableBody>
                      <TableRow className="peer-hover:bg-gray-50 dark:peer-hover:bg-gray-800">
                        <TableCell>alice@example.com</TableCell>
                        <TableCell>Admin</TableCell>
                        <TableCell>Manage Users</TableCell>
                      </TableRow>
                      <TableRow className="peer-hover:bg-gray-50 dark:peer-hover:bg-gray-800">
                        <TableCell>bob@example.com</TableCell>
                        <TableCell>User</TableCell>
                        <TableCell>View Reports</TableCell>
                      </TableRow>
                    </TableBody>
                  </Table>
                </div>
              </CardContent>
            </Card>
            <Card>
              <CardHeader className="pb-0">
                <CardTitle>System Configuration</CardTitle>
                <CardDescription>Configure SIEM settings and integrations.</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid gap-4">
                  <div className="flex items-center space-x-4">
                    <Label
                      className="min-w-[200px] text-sm peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                      htmlFor="data-retention"
                    >
                      Data Retention (days)
                    </Label>
                    <Input className="w-1/2" defaultValue="30" id="data-retention" placeholder="Data Retention" />
                  </div>
                  <div className="flex items-center space-x-4">
                    <Label
                      className="min-w-[200px] text-sm peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                      htmlFor="log-level"
                    >
                      Log Level
                    </Label>
                    <Select
                      className="min-w-[200px] peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                      id="log-level"
                    >
                      <option value="info">Info</option>
                      <option value="warning">Warning</option>
                      <option value="error">Error</option>
                    </Select>
                  </div>
                </div>
              </CardContent>
            </Card>
            <Card>
              <CardHeader className="pb-0">
                <CardTitle>Alerts & Notifications</CardTitle>
                <CardDescription>Customize alert thresholds and notification channels.</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid gap-4">
                  <div className="flex items-center space-x-4">
                    <Label
                      className="min-w-[200px] text-sm peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                      htmlFor="alert-threshold"
                    >
                      Alert Threshold
                    </Label>
                    <Select
                      className="min-w-[200px] peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                      id="alert-threshold"
                    >
                      <option value="1">1</option>
                      <option value="5">5</option>
                      <option value="10">10</option>
                    </Select>
                  </div>
                  <fieldset className="border p-4 rounded-lg peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                    <legend className="font-medium">Notification Channels</legend>
                    <div className="grid grid-cols-3 gap-4">
                      <Label className="flex items-center" htmlFor="email">
                        <Checkbox className="peer:hidden" id="email" />
                        Email
                      </Label>
                      <Label className="flex items-center" htmlFor="sms">
                        <Checkbox className="peer:hidden" id="sms" />
                        SMS
                      </Label>
                      <Label className="flex items-center" htmlFor="slack">
                        <Checkbox className="peer:hidden" id="slack" />
                        Slack
                      </Label>
                    </div>
                  </fieldset>
                </div>
              </CardContent>
              <CardFooter className="border-t p-6">
                <Button>Save Changes</Button>
              </CardFooter>
            </Card>
          </div>
        </div>
      </main>
    </div>
  )
}


function FrameIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <line x1="22" x2="2" y1="6" y2="6" />
      <line x1="22" x2="2" y1="18" y2="18" />
      <line x1="6" x2="6" y1="2" y2="22" />
      <line x1="18" x2="18" y1="2" y2="22" />
    </svg>
  )
}