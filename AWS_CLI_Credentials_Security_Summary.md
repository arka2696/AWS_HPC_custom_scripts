
# Securing AWS CLI Credentials on a Shared Computer

When using a shared computer to upload files to AWS S3, it’s important to protect AWS credentials from unauthorized access or deletion. Here are several methods to enhance security:

## 1. Restrict File Permissions
Use Windows file permissions on the `credentials` and `config` files to restrict access. Set **Read & Execute** permissions for users who need to use the profile but shouldn't modify or delete it.

**Steps:**
- Navigate to `%USERPROFILE%\.aws`.
- Right-click the `credentials` file, select **Properties**, then go to the **Security** tab.
- Adjust permissions to allow only authorized users to modify the file.
- Repeat for the `config` file if needed.

## 2. Use Temporary Environment Variables
Instead of storing permanent credentials, each user can set AWS credentials as environment variables temporarily for their session.

**Example Commands:**
```cmd
set AWS_ACCESS_KEY_ID=your_access_key_id
set AWS_SECRET_ACCESS_KEY=your_secret_access_key
```
After uploading files, users can clear the variables:
```cmd
set AWS_ACCESS_KEY_ID=
set AWS_SECRET_ACCESS_KEY=
```

## 3. Use AWS SSO or IAM Role with Temporary Credentials
For higher security, consider using AWS Single Sign-On (SSO) or IAM roles with `aws sts assume-role` for temporary credentials. This eliminates the need for long-term access keys on the shared machine.

- **AWS SSO**: Users authenticate via a web portal, receiving temporary credentials without storing them.
- **IAM Assume Role**: Users obtain temporary credentials via a command, reducing credential exposure.

## 4. Automate Credential Management
Use a script that prompts users for credentials, uses them temporarily, and then deletes or rotates them after the session. This ensures that credentials are not left accessible to subsequent users.

---
These methods help secure AWS CLI credentials in a shared environment, with options to prevent unauthorized modification and protect sensitive information.
